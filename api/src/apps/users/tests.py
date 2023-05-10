from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import AllowedEmail


User = get_user_model()


class UserProfileTests(TestCase):
    def test_create_allowed_user(self):
        AllowedEmail.objects.create(email='example@example.com')

        user = User(
            email='example@example.com',
            password='pass',
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich',
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.email, 'example@example.com')
        self.assertEqual(user.first_name, 'Ivan')
        self.assertEqual(user.last_name, 'Ivanov')
        self.assertEqual(user.patronymic, 'Ivanovich')

    def test_create_not_allowed_user(self):
        user = User(
            email='example2@example.com',
            password='pass',
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich',
        )

        with self.assertRaises(ValidationError):
            user.full_clean()
            user.save()

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email='admin@example.com',
            password='admin'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_superuser_incorrect(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='admin2@example.com',
                password='admin',
                is_staff=False,
                is_superuser=False
            )
