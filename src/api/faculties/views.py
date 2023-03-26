from rest_framework import viewsets
from rest_framework import permissions

from . import models
from . import serializers


class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    """Faculty view set that only allows to read all faculty instances
    for all users (including unauthorized).
    """

    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    permission_classes = (permissions.AllowAny, )
