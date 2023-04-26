from django.contrib.auth import get_user_model
from django.test import TestCase

from .exceptions import NotAllowedEmailValidationError
from .models import AllowedEmail


User = get_user_model()


class CustomUserTests(TestCase):
    def test_create_allowed_customuser(self):
        AllowedEmail.objects.create(email='example@example.com')

        user = User.objects.create(
            username='user',
            password='pass',
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich',
            email='example@example.com'
        )

        self.assertEqual(user.first_name, 'Ivan')
        self.assertEqual(user.last_name, 'Ivanov')
        self.assertEqual(user.patronymic, 'Ivanovich')
        self.assertEqual(user.email, 'example@example.com')

    def test_create_no_allowed_customuser(self):
        with self.assertRaises(NotAllowedEmailValidationError):
            User.objects.create(
                username='user2',
                password='pass',
                first_name='Ivan',
                last_name='Ivanov',
                patronymic='Ivanovich',
                email='example2@example.com'
            )
