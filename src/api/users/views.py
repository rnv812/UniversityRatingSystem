from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers as custom_serializers


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """User view set that only allows to read all user instances for admins
    and get own instance for non admins (authorized users).
    """

    queryset = models.CustomUser.objects.all()
    serializer_class = custom_serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser, )

    @action(detail=False, methods=permissions.SAFE_METHODS, permission_classes=(permissions.IsAuthenticated, ))
    def me(self, request):
        return Response(custom_serializers.UserSerializer(instance=request.user).data)
