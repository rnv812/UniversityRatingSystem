from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import ValueType, RatingPartition, Indicator, Criterion
from .serializers import (ValueTypeSerializer,
                          RatingPartitionSerializer,
                          IndicatorSerializer,
                          CriterionSerializer)


class ValueTypeViewSet(ReadOnlyModelViewSet):
    queryset = ValueType.objects.all().order_by('pk')
    serializer_class = ValueTypeSerializer
    permission_classes = (AllowAny, )


class RatingPartitionViewSet(ReadOnlyModelViewSet):
    queryset = RatingPartition.objects.all().order_by('pk')
    serializer_class = RatingPartitionSerializer
    permission_classes = (AllowAny, )


class IndicatorViewSet(ReadOnlyModelViewSet):
    queryset = Indicator.objects.all().order_by('pk')
    serializer_class = IndicatorSerializer
    permission_classes = (AllowAny, )


class CriterionViewSet(ReadOnlyModelViewSet):
    queryset = Criterion.objects.all().order_by('pk')
    serializer_class = CriterionSerializer
    permission_classes = (AllowAny, )
