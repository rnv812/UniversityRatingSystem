from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', )
    search_fields = ('name', 'head__last_name', )
    search_help_text = _('Faculty name or head last name')
