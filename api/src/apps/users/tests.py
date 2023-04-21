from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class CustomUserTests(TestCase):
    def test_create_customuser(self):
        user = User.objects.create(
            username='user',
            password='pass',
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich'
        )

        self.assertEqual(user.first_name, 'Ivan')
        self.assertEqual(user.last_name, 'Ivanov')
        self.assertEqual(user.patronymic, 'Ivanovich')
