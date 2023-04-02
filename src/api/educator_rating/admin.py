from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (EducatorRatingPartition,
                     EducatorIndicatorValue,
                     EducatorReport,
                     EducatorReportController)


@admin.register(EducatorRatingPartition)
class EducatorRatingPartitionAdmin(admin.ModelAdmin):
    list_display = ('partition', )


@admin.register(EducatorIndicatorValue)
class EducatorIndicatorValueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'report', 'indicator', )


@admin.register(EducatorReport)
class EducatorReportAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'year', 'approved', )
    search_fields = (
        'educator__user__first_name', 'educator__user__last_name',
        'educator__user__patronymic',
    )
    list_select_related = ('educator__user', 'educator__qualification')
    search_help_text = _('Educator first name, lastname or patronymic')
    list_filter = ('educator__qualification__name', 'year', )


@admin.register(EducatorReportController)
class EducatorReportControllerAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', )
    search_fields = (
        'user__username', 'user__first_name', 'user__last_name',
        'user__patronymic', 'department__name',
    )
    search_help_text = _(
        ('Department name or controller username, '
         'first name, last name or patronymic')
    )
