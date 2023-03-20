from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms
from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser

    list_display = ('username', 'last_name', 'first_name', 'patronymic', )
