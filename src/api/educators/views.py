from rest_framework import viewsets
from rest_framework import permissions

from . import models
from . import serializers


class EducatorViewSet(viewsets.ReadOnlyModelViewSet):
    """Educator view set that only allows to read all educator instances
    for all users (including unauthorized).
    """

    queryset = models.Educator.objects.all()
    serializer_class = serializers.EducatorSerializer
    permission_classes = (permissions.AllowAny, )
