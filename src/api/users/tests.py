from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UsersManagerTests(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            username='user',
            password='pass',
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich'
        )

        self.assertEqual(user.patronymic, 'Ivanovich')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username='admin',
            password='pass',
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich'
        )

        self.assertEqual(admin_user.patronymic, 'Ivanovich')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(username='admin2', password='pass', is_superuser=False)

    def test_get_full_name(self):
        user = User.objects.create(
            username='user2',
            password='pass',
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich'
        )

        self.assertEqual(user.get_full_name(), 'Ivanov Ivan Ivanovich')
