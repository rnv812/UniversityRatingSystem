from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .exceptions import NotAllowedEmailValidationError


class AllowedEmail(models.Model):
    """Model stores emails of users that are allowed to register."""

    email = models.EmailField(verbose_name=_('email address'))

    class Meta:
        verbose_name = _('allowed email')
        verbose_name = _('allowed emails')

    def __str__(self) -> str:
        return f'{self.email}'


class CustomUser(AbstractUser):
    """Custom user model with `patronomyc` field
    and mandatory first_name, last_name and email fields.
    """

    first_name = models.CharField(verbose_name=_('first name'), max_length=150)
    last_name = models.CharField(verbose_name=_('last name'), max_length=150)
    patronymic = models.CharField(verbose_name=_('patronomyc'), max_length=150)
    email = models.EmailField(verbose_name=_('email address'))

    def get_full_name(self) -> str:
        """Return the last_name plus the first_name plus the patronymic,
        with a space in between.
        """
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def clean(self) -> None:
        try:
            AllowedEmail.objects.get(email=self.email)
        except AllowedEmail.DoesNotExist:
            raise NotAllowedEmailValidationError(
                message=_('Email is not in allowed list')
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save()
