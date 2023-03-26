from rest_framework import viewsets
from rest_framework import permissions

from . import models
from . import serializers


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """Department view set that only allows to read all department instances
    for all users (including unauthorized).
    """

    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = (permissions.AllowAny, )
