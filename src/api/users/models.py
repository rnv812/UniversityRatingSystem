from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Base User model with patronomyc field."""
    patronymic = models.CharField(_('patronomyc'), max_length=150, blank=True)

    def get_full_name(self) -> str:
        """Return the last_name plus the first_name plus the patronymic, with a space in between."""
        full_name = "%s %s %s" % (self.last_name, self.first_name, self.patronymic)
        return full_name.strip()
