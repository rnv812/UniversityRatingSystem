from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form for creation CustomUser model instance."""

    class Meta:
        model = CustomUser
        fields = ('patronymic', )


class CustomUserChangeForm(UserChangeForm):
    """Form for changing CustomUser model instance."""

    class Meta:
        models = CustomUser
        fields = ('patronymic', )
