from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.apps import AuthConfig
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import AllowedEmail, CustomUser


# change name cause User model is not in this app anymore. So only "Groups".
AuthConfig.verbose_name = _('Groups')


@admin.register(AllowedEmail)
class AllowedEmailAdmin(admin.ModelAdmin):
    list_display = ('email', )
    search_fields = ('email', )
    search_help_text = _('Email address')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = (
        'username', 'email', 'last_name', 'first_name', 'patronymic',
    )
    search_fields = (
        'username', 'email', 'last_name', 'first_name', 'patronymic',
    )
    search_help_text = _(
        'Username, first name, last name, patronymic or email'
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            _('Personal info'),
            {
                'fields': (
                    'last_name', 'first_name', 'patronymic', 'email',
                )
            }
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username', 'email', 'last_name', 'first_name',
                    'patronymic', 'password1', 'password2',
                ),
            },
        ),
    )
