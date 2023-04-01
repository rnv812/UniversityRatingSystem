from rest_framework.serializers import ModelSerializer

from .models import ValueType, RatingPartition, Indicator, Criterion


class ValueTypeSerializer(ModelSerializer):
    class Meta:
        model = ValueType
        fields = ('id', 'name', )


class RatingPartitionSerializer(ModelSerializer):
    class Meta:
        model = RatingPartition
        fields = ('id', 'name', 'abbreviation', )


class IndicatorSerializer(ModelSerializer):
    class Meta:
        model = Indicator
        fields = (
            'id', 'name', 'annotation',
            'value_type_id', 'staff_only_editable',
        )


class CriterionSerializer(ModelSerializer):
    class Meta:
        model = Criterion
        fields = (
            'id', 'partition_id', 'number', 'subnumber',
            'indicator_id', 'weight',
        )
