from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractUser, BaseUserManager)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver

from ..integration_1c.queries import query_mock_employee_data


class AllowedEmail(models.Model):
    """Model stores emails of users that are allowed to register."""

    email = models.EmailField(verbose_name=_('email address'), unique=True)
    employee_id = models.CharField(
        verbose_name=_('employee id'),
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = _('allowed email')
        verbose_name_plural = _('allowed emails')

    def __str__(self) -> str:
        return f'{self.email}'

    @staticmethod
    def validate_email(email):
        try:
            AllowedEmail.objects.get(email=email)
        except AllowedEmail.DoesNotExist:
            raise ValidationError(
                message=_('Email is not in allowed list')
            )


class UserProfileManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email, and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class UserProfile(AbstractUser):
    """Custom user model which uses email as username and has `patronomyc`
    `first_name`, `last_name` mandatory fields.
    """
    username = None

    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        validators=[AllowedEmail.validate_email]
    )
    first_name = models.CharField(verbose_name=_('first name'), max_length=150)
    last_name = models.CharField(verbose_name=_('last name'), max_length=150)
    patronymic = models.CharField(
        verbose_name=_('patronomyc'),
        max_length=150,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserProfileManager()

    def __str__(self) -> str:
        return f'{self.email}'

    def get_full_name(self) -> str:
        """Return the last_name plus the first_name plus the patronymic,
        with a space in between.
        """
        full_name = f'{self.last_name} {self.first_name} {self.patronymic}'
        return full_name.strip()


@receiver(models.signals.post_save, sender=UserProfile)
def add_data_from_integration_server(
    sender,
    instance,
    created,
    *args,
    **kwargs
) -> None:
    # We check if for specified email also employee id provided
    # if so we can fetch data from employee server and set such data as:
    # first_name, last_name, patronymic, is_active
    # also we can create a new educator
    if not created:
        return

    employee_id = AllowedEmail.objects.get(email=instance.email).employee_id

    if not employee_id:
        return

    # To avoid circular dependecies imports goes here
    from ..integration_1c.constructors import (construct_educator_data,
                                               construct_user_data,
                                               create_educator_hook)

    employee_data = query_mock_employee_data(employee_id)

    user_data = construct_user_data(employee_data)

    if user_data:
        instance.last_name = user_data.last_name
        instance.first_name = user_data.first_name
        instance.patronymic = user_data.patronymic
        instance.save(update_fields=['last_name', 'first_name', 'patronymic'])

    educator_data = construct_educator_data(employee_data)

    if educator_data:
        create_educator_hook(
            user=instance,
            qualification=educator_data.qualification,
            department=educator_data.department
        )
