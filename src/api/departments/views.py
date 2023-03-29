from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import SAFE_METHODS, AllowAny
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

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
