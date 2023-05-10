from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Department, DepartmentType
from .serializers import DepartmentSerializer, DepartmentTypeSerializer


class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset = Department.objects.all().order_by('pk')
    serializer_class = DepartmentSerializer


class DepartmentTypeViewSet(ReadOnlyModelViewSet):
    queryset = DepartmentType.objects.all().order_by('pk')
    serializer_class = DepartmentTypeSerializer
