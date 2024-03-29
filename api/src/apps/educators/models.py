from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.departments.models import Department
from apps.users.models import UserProfile


class Qualification(models.Model):
    """Model represents educator qualification."""

    name = models.CharField(
        verbose_name=_('qualification name'),
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = _('qualification')
        verbose_name_plural = _('qualifications')

    def __str__(self) -> str:
        return self.name


class Educator(models.Model):
    """Model represents university educator."""

    user = models.OneToOneField(
        verbose_name=_('educator profile'),
        to=UserProfile,
        on_delete=models.PROTECT
    )

    qualification = models.ForeignKey(
        verbose_name=_('educator qualification'),
        to=Qualification,
        on_delete=models.PROTECT
    )
    department = models.ForeignKey(
        verbose_name=_('educator department'),
        to=Department,
        on_delete=models.PROTECT
    )

    scopus_id = models.CharField(
        verbose_name=_('Scopus ID'),
        max_length=11,
        blank=True
    )

    wos_id = models.CharField(
        verbose_name=_('Web of Science ID'),
        max_length=13,
        blank=True
    )

    class Meta:
        verbose_name = _('educator')
        verbose_name_plural = _('educators')

    def __str__(self) -> str:
        return f'{self.user.get_full_name()}'
