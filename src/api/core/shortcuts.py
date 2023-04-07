from django.shortcuts import get_object_or_404
from django.http.response import Http404

from rest_framework.exceptions import ValidationError


def get_object_or_validation_error(
        exception: ValidationError,
        klass,
        *args,
        **kwargs
):
    """Use get() to return an object, or raise ValidationError instance
    passed as `error` parameter if the object does not exist. Can be used as
    generic version of get_object_or_404 in context of django rest framework.

    Use get_object_or_404 django shortcut for not to reimplement logic.
    """

    try:
        return get_object_or_404(klass, *args, **kwargs)
    except Http404:
        raise exception
