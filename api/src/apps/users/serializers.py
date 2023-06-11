from rest_framework.serializers import ModelSerializer

from .models import AllowedEmail, UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id', 'email',
            'last_name', 'first_name', 'patronymic',
            'is_active', 'is_staff', 'is_superuser',
            'date_joined', 'last_login',
        )


class AllowedEmailSerializer(ModelSerializer):
    class Meta:
        model = AllowedEmail
        fields = ('id', 'email', 'employee_id', )
