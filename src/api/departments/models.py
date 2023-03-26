from django.db import models
from django.utils.translation import gettext_lazy as _

from api.faculties.models import Faculty
from api.users.models import CustomUser


class DepartmentType(models.Model):
    """Model that represents type of university department."""

    name = models.CharField(verbose_name=_('department type name'), max_length=100, unique=True)

    class Meta:
        verbose_name = _('department type')
        verbose_name_plural = _('department types')

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    """Model that represents university department."""

    name = models.CharField(verbose_name=_('department name'), max_length=255, unique=True)
    department_type = models.ForeignKey(verbose_name=_('department type'), to=DepartmentType, on_delete=models.PROTECT)
    head = models.OneToOneField(verbose_name=_('department head profile'), to=CustomUser, on_delete=models.PROTECT)
    faculty = models.ForeignKey(verbose_name=_('department faculty'), to=Faculty, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')

    def __str__(self) -> str:
        return self.name
