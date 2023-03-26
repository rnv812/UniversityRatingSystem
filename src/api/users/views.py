from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    """User view set that only allows to read all user instances for admins.
    Non admin users can only get their own instance.
    """

    queryset = CustomUser.objects.all().order_by('pk')
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )

    @action(detail=False, methods=SAFE_METHODS, permission_classes=(IsAuthenticated, ))
    def me(self, request):
        """Respond user with his own instance."""
        return Response(UserSerializer(instance=request.user).data)
