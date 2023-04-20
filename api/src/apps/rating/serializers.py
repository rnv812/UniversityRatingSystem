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
            'value_type', 'privileged',
        )


class CriterionSerializer(ModelSerializer):
    class Meta:
        model = Criterion
        fields = (
            'id', 'partition', 'number', 'subnumber',
            'indicator', 'weight',
        )
