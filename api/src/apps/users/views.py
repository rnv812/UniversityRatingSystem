from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all().order_by('pk')
    serializer_class = UserSerializer

    @action(
        detail=False,
        methods=SAFE_METHODS,
        permission_classes=(IsAuthenticated, ),
        url_name='user_me'
    )
    def me(self, request: Request) -> Response:
        """Respond user with his own instance."""

        return Response(UserSerializer(instance=request.user).data)
