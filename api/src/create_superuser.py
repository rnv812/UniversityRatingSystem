# instead of using python manage.py createsuper --no-input
# we use this script because we need to add superuser email
# to allowed list (create AllowedEmail instance) initially

import os

from apps.users.models import AllowedEmail, UserProfile


email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
AllowedEmail.objects.create(email=email)
UserProfile.objects.create_superuser(
    email=email,
    password=password,
    is_superuser=True,
    is_staff=True,
)
