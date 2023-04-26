from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.apps import AuthConfig
from django.utils.translation import gettext_lazy as _

from .forms import UserProfileChangeForm, UserProfileCreationForm
from .models import AllowedEmail, UserProfile


# change name cause User model is not in this app anymore. So only "Groups".
AuthConfig.verbose_name = _('Groups')


@admin.register(AllowedEmail)
class AllowedEmailAdmin(admin.ModelAdmin):
    list_display = ('email', )
    search_fields = ('email', )
    search_help_text = _('Email address')


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    form = UserProfileChangeForm
    add_form = UserProfileCreationForm

    ordering = ('email',)

    list_display = (
        'email', 'last_name', 'first_name', 'patronymic',
    )
    search_fields = (
        'email', 'last_name', 'first_name', 'patronymic',
    )
    search_help_text = _(
        'Email, first name, last name or patronymic'
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal info'),
            {
                'fields': (
                    'last_name', 'first_name', 'patronymic',
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
                    'email', 'last_name', 'first_name', 'patronymic',
                    'password1', 'password2',
                ),
            },
        ),
    )
