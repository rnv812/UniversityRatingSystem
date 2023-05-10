from typing import Iterable, Optional
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.departments.models import Department
from apps.educators.models import Educator
from apps.rating.models import Criterion, Indicator, RatingPartition
from apps.rating.validators import validate_indicator_value
from apps.users.models import UserProfile

from .fields import ValidRatingYearField


class EducatorRatingPartition(models.Model):
    """Model describes which rating partitions is used for educator rating.
    Each instance of this model relates to the specific partition and for all
    criterions in this partition EducatorIndicatorValue instances will be
    created to relate them to the EducatorReport instance.
    """

    partition = models.OneToOneField(
        verbose_name=_("rating partition"),
        to=RatingPartition,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("educator rating partition")
        verbose_name_plural = _("educator rating partitions")

    def __str__(self) -> str:
        return f'{self.partition}'


class EducatorReport(models.Model):
    """Model relates different indicator values to one instance and contains
    data about when values were entered and who is the educator who entered.
    """

    uuid = models.UUIDField(
        verbose_name=_('report UUID'),
        auto_created=True,
        editable=False,
        unique=True,
        default=uuid4
    )
    educator = models.ForeignKey(
        verbose_name=_('educator'),
        to=Educator,
        on_delete=models.CASCADE
    )
    year = ValidRatingYearField(verbose_name=_('report year'))
    approved = models.BooleanField(
        verbose_name=_('report approved status'),
        default=False
    )

    class Meta:
        verbose_name = _('report')
        verbose_name_plural = _('reports')
        unique_together = ('educator', 'year', )

    def __str__(self) -> str:
        return f"{self.educator} {self.year} {_('year')}"

    def save(
            self,
            force_insert: bool = False,
            force_update: bool = False,
            using: Optional[str] = None,
            update_fields: Optional[Iterable[str]] = None
    ) -> None:
        super().save(force_insert, force_update, using, update_fields)

        # attach default indicator values to report
        partition_ids = EducatorRatingPartition.objects.values_list(
            'partition_id',
            flat=True
        )
        indicator_ids = Criterion.objects.filter(
            partition_id__in=partition_ids
        ).distinct(
            'indicator_id'
        ).values_list('indicator_id', flat=True)

        indicator_values = []
        indicators = Indicator.objects.filter(pk__in=indicator_ids)

        for id in indicator_ids:
            indicator = indicators.get(pk=id)
            indicator_values.append(
                EducatorIndicatorValue(
                    indicator=indicator,
                    value=indicator.value_type.get_default(),
                    report=self,
                )
            )

        EducatorIndicatorValue.objects.bulk_create(indicator_values)


class EducatorIndicatorValue(models.Model):
    """Model represents the value of indicator that included in educator
    rating partitions (via criterions). Instances of this model are linked
    to the corresponding EducatorReport instance to relate them together.
    """

    indicator = models.ForeignKey(
        verbose_name=_('indicator'),
        to=Indicator,
        on_delete=models.CASCADE
    )
    value = models.JSONField(
        verbose_name=_('indicator value'),
        validators=(validate_indicator_value, )
    )
    report = models.ForeignKey(
        verbose_name=_('educator report'),
        to=EducatorReport,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('indicator value')
        verbose_name_plural = _('indicator values')
        unique_together = ('indicator', 'report')

    def __str__(self) -> str:
        return f'{self.value}'


class EducatorReportController(models.Model):
    """Model represents a user who is able to inspect and approve reports
    of educators at the department which he is assigned to."""

    user = models.ForeignKey(
        verbose_name=_('controller profile'),
        to=UserProfile,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        verbose_name=_('responsible department'),
        to=Department,
        on_delete=models.CASCADE,
        related_name='educator_report_controllers'
    )

    class Meta:
        verbose_name = _('controller')
        verbose_name_plural = _('controllers')
        unique_together = ('user', 'department', )

    def __str__(self) -> str:
        return f'{self.user}'
