from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EducatorsRatingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.educators_rating'
    verbose_name = _('educators rating')
