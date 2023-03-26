from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import SAFE_METHODS, AllowAny
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Department, DepartmentType
from .serializers import DepartmentSerializer, DepartmentTypeSerializer


class DepartmentViewSet(ReadOnlyModelViewSet):
    """Department view set that only allows to read all department instances
    for all users (including unauthorized).
    """

    queryset = Department.objects.all().order_by('pk')
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny, )

    @action(detail=False, methods=SAFE_METHODS, permission_classes=(AllowAny, ))
    def types(self, request: Request) -> Response:
        return Response(
            DepartmentTypeSerializer(
                instance=DepartmentType.objects.all().order_by('pk'),
                many=True
            ).data
        )
