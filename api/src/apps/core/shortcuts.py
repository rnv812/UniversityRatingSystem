from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException


def get_object_or_error(
        exception: APIException,
        klass,
        *args,
        **kwargs
):
    """Use get() to return an object, or raise APIException instance
    passed as first parameter if the object does not exist. Can be used as
    generic version of get_object_or_404 in context of django rest framework.
    """

    try:
        return get_object_or_404(klass, *args, **kwargs)
    except Http404:
        raise exception
