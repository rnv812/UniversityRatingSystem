from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ValueType, RatingPartition, Indicator, Criterion


@admin.register(ValueType)
class ValueTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'datatype', )
    list_filter = ('datatype', )


@admin.register(RatingPartition)
class RatingPartitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', )


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'annotation',
        'value_type', 'privileged',
    )
    search_fields = ('name', )
    search_help_text = _('Indicator name')
    list_filter = ('value_type__name', 'privileged')


@admin.register(Criterion)
class CriterionAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'partition', 'number', 'subnumber', 'indicator', 'weight',
    )
    search_fields = ('indicator__name', )
    search_help_text = _('Indicator name')
    list_filter = ('partition__name', )
