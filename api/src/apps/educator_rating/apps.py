from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EducatorRatingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.educator_rating'
    verbose_name = _('Educator rating')
