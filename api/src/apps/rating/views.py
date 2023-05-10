from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Criterion, Indicator, RatingPartition, ValueType
from .serializers import (CriterionSerializer, IndicatorSerializer,
                          RatingPartitionSerializer, ValueTypeSerializer)


class ValueTypeViewSet(ReadOnlyModelViewSet):
    queryset = ValueType.objects.all().order_by('pk')
    serializer_class = ValueTypeSerializer


class RatingPartitionViewSet(ReadOnlyModelViewSet):
    queryset = RatingPartition.objects.all().order_by('pk')
    serializer_class = RatingPartitionSerializer

    @action(
        detail=True,
        methods=SAFE_METHODS
    )
    def criterions(self, request: Request, pk: str) -> Response:
        """Get list of criterions in specifid partition."""

        partition = get_object_or_404(RatingPartition, pk=pk)

        criterion_pks = Criterion.objects.filter(
            partition=partition
        ).values_list('pk', flat=True)

        return Response(criterion_pks)


class IndicatorViewSet(ReadOnlyModelViewSet):
    queryset = Indicator.objects.all().order_by('pk')
    serializer_class = IndicatorSerializer


class CriterionViewSet(ReadOnlyModelViewSet):
    queryset = Criterion.objects.all().order_by('pk')
    serializer_class = CriterionSerializer
