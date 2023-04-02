from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Educator, Qualification


@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'qualification', 'department', )
    search_fields = (
        'department__name', 'user__first_name', 'user__last_name',
        'user__patronymic', 'user__username',
    )
    search_help_text = _(
        ('Department name or educator username, '
         'first name, last name or patronymic')
    )
    list_filter = ('qualification__name', )


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('name', )
