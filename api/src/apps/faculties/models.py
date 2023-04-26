from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import UserProfile


class Faculty(models.Model):
    """Model represents university faculty."""

    name = models.CharField(
        verbose_name=_('faculty name'),
        max_length=255,
        unique=True
    )
    head = models.ForeignKey(
        verbose_name=_('faculty head profile'),
        to=UserProfile,
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _('faculty')
        verbose_name_plural = _('faculties')

    def __str__(self) -> str:
        return self.name
