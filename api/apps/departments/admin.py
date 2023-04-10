from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Department, DepartmentType


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'department_type', 'faculty', )
    search_fields = (
        'name', 'head__first_name', 'head__last_name', 'head__patronymic',
    )
    search_help_text = _(
        'Department name or head first name, last name or patronymic'
    )
    list_filter = ('department_type__name', 'faculty__name', )
    autocomplete_fields = ('department_type', 'head', 'faculty', )


@admin.register(DepartmentType)
class DepartmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    search_help_text = _('Department type name')
