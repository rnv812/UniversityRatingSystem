from rest_framework import viewsets
from rest_framework import permissions

from . import models
from . import serializers


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser, )
