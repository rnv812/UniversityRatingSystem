from django.core.exceptions import ValidationError


class NotAllowedEmailValidationError(ValidationError):
    pass
