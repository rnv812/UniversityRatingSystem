from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import Department, DepartmentType
from .serializers import DepartmentSerializer, DepartmentTypeSerializer


class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset = Department.objects.all().order_by('pk')
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny, )


class DepartmentTypeViewSet(ReadOnlyModelViewSet):
    queryset = DepartmentType.objects.all().order_by('pk')
    serializer_class = DepartmentTypeSerializer
    permission_classes = (AllowAny, )
