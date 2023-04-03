from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

from .routers import api_router


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include((api_router.urls, 'api'), namespace='api')),
]

urlpatterns_debug = [
    path(
        'schema/',
        get_schema_view(
            title='University Rating System API',
            description=(
                'API for performing operations on rating reports.'
            ),
            version='1.0.0',
        ),
        name='api-schema'
    ),
    path(
        'swagger/',
        TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'api-schema'}
        ),
        name='swagger'
    ),
]

if settings.DEBUG:
    urlpatterns.extend(urlpatterns_debug)
