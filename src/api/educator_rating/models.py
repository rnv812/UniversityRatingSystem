from django.db import models
from django.utils.translation import gettext_lazy as _

from api.rating.models import RatingPartition, Indicator
from api.educators.models import Educator

from uuid import uuid4

from .fields import ValidRatingYearField
from api.users.models import CustomUser
from api.departments.models import Department


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
        verbose_name = _('educator report')
        verbose_name_plural = _('educator reports')
        unique_together = ('educator', 'year', )

    def __str__(self) -> str:
        return f"{self.educator} {self.year} {_('year')}"


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
    value = models.JSONField(verbose_name=_('indicator value'))
    report = models.ForeignKey(
        verbose_name=_('educator report'),
        to=EducatorReport,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('educator indicator value')
        verbose_name_plural = _('educator indicator values')

    def __str__(self) -> str:
        return f'{self.value}'


class EducatorReportController(models.Model):
    """Model represents a user who is able to inspect and approve reports
    of educators at the department which he is assigned to."""

    user = models.ForeignKey(
        verbose_name=_('controller profile'),
        to=CustomUser,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        verbose_name=_('responsible department'),
        to=Department,
        on_delete=models.CASCADE,
        related_name='educator_report_controllers'
    )

    class Meta:
        verbose_name = _('educator report controller')
        verbose_name_plural = _('educator report controllers')
        unique_together = ('user', 'department', )

    def __str__(self) -> str:
        return f'{self.user}'
