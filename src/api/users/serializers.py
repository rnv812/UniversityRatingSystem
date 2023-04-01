from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'email',
            'last_name', 'first_name', 'patronymic',
            'is_active', 'is_staff', 'is_superuser',
            'date_joined', 'last_login',
        )
