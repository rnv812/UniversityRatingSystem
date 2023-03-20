from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . import models


class CustomUserCreationForm(UserCreationForm):
    """Base UserCreateForm with patronymic field."""

    class Meta:
        model = models.CustomUser
        fields = ('patronymic', )


class CustomUserChangeForm(UserChangeForm):
    """Base UserChangeForm with patronymic field."""

    class Meta:
        models = models.CustomUser
        fields = ('patronymic', )
