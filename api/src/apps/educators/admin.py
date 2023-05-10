from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Educator, Qualification


@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'qualification', 'department', )
    search_fields = (
        'department__name', 'user__first_name', 'user__last_name',
        'user__patronymic', 'user__email',
    )
    search_help_text = _(
        ('Department name or educator email, '
         'first name, last name or patronymic')
    )
    list_filter = ('qualification__name', )
    autocomplete_fields = ('user', 'qualification', 'department', )


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    search_help_text = _('Qualification name')
