from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    """Form for creation UserProfile model instance."""

    class Meta:
        model = UserProfile
        fields = ('email', )


class UserProfileChangeForm(UserChangeForm):
    """Form for changing UserProfile model instance."""

    class Meta:
        model = UserProfile
        fields = ('email', )
