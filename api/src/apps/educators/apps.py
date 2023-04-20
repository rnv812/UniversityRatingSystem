from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EducatorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.educators'
    verbose_name = _('Educators')
