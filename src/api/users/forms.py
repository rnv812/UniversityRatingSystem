from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . import models


class CustomUserCreationForm(UserCreationForm):
    """Form for creation CustomUser model instance."""

    class Meta:
        model = models.CustomUser
        fields = ('patronymic', )


class CustomUserChangeForm(UserChangeForm):
    """Form for changing CustomUser model instance."""

    class Meta:
        models = models.CustomUser
        fields = ('patronymic', )
