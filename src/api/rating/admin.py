from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ValueType, RatingPartition, Indicator, Criterion


@admin.register(ValueType)
class ValueTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(RatingPartition)
class RatingPartitionAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'annotation',
        'value_type', 'staff_only_editable',
    )
    search_fields = ('name', )
    search_help_text = _('Indicator name')
    list_filter = ('value_type__name', 'staff_only_editable')


@admin.register(Criterion)
class CriterionAdmin(admin.ModelAdmin):
    list_display = (
        'partition', 'number', 'subnumber',
        'indicator', 'weight',
    )
    search_fields = ('indicator__name', )
    search_help_text = _('Indicator name')
    list_filter = ('partition__name', )
