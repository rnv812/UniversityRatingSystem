from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Custom user model with `patronomyc` field."""

    first_name = models.CharField(verbose_name=_('first name'), max_length=150)
    last_name = models.CharField(verbose_name=_('last name'), max_length=150)
    patronymic = models.CharField(verbose_name=_('patronomyc'), max_length=150)

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        """Return the last_name plus the first_name plus the patronymic, with a space in between."""
        full_name = "%s %s %s" % (self.last_name, self.first_name, self.patronymic)
        return full_name.strip()
