from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from rest_framework.authtoken.models import TokenProxy
from rest_framework.authtoken.admin import TokenAdmin

TokenProxy._meta.verbose_name = _('token')
TokenProxy._meta.verbose_name_plural = _('tokens')

admin.site.unregister(TokenProxy)


# https://github.com/encode/django-rest-framework/discussions/8927
@admin.register(TokenProxy)
class TokenCustomAdmin(TokenAdmin):
    search_fields = ('user__username', )
    search_help_text = _('Username')


admin.site.site_header = _('API Administration')
admin.site.site_title = _('API Administration')
admin.site.index_title = _('API Administration')
