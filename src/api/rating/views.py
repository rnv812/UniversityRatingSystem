from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Criterion, Indicator, RatingPartition, ValueType
from .serializers import (
    CriterionSerializer,
    IndicatorSerializer,
    RatingPartitionSerializer,
    ValueTypeSerializer,
)


class ValueTypeViewSet(ReadOnlyModelViewSet):
    queryset = ValueType.objects.all().order_by('pk')
    serializer_class = ValueTypeSerializer


class RatingPartitionViewSet(ReadOnlyModelViewSet):
    queryset = RatingPartition.objects.all().order_by('pk')
    serializer_class = RatingPartitionSerializer


class IndicatorViewSet(ReadOnlyModelViewSet):
    queryset = Indicator.objects.all().order_by('pk')
    serializer_class = IndicatorSerializer


class CriterionViewSet(ReadOnlyModelViewSet):
    queryset = Criterion.objects.all().order_by('pk')
    serializer_class = CriterionSerializer
