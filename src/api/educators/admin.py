from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Educator, Qualification


@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'qualification', 'department', )
    search_fields = (
        'user__first_name', 'user__last_name', 'user__patronymic',
    )


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('name', )
