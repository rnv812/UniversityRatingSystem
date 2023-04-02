from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Custom user model with `patronomyc` field
    and mandatory first_name and last_name fields.
    """

    first_name = models.CharField(verbose_name=_('first name'), max_length=150)
    last_name = models.CharField(verbose_name=_('last name'), max_length=150)
    patronymic = models.CharField(verbose_name=_('patronomyc'), max_length=150)

    def get_full_name(self) -> str:
        """Return the last_name plus the first_name plus the patronymic,
        with a space in between.
        """
        return f'{self.last_name} {self.first_name} {self.patronymic}'
