import os
from uuid import uuid4

from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', include('apps.core.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
else:
    urlpatterns.append(
        path(
            f'{os.getenv("ADMIN_SITE_URL", str(uuid4()))}/',
            admin.site.urls
        )
    )
