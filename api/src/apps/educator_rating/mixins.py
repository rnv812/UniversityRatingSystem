from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class PartialUpdateModelMixin:
    """Update a model instance. Only PATCH method is allowed."""

    def partial_update(self, request: Request, *args, **kwargs) -> Response:
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer: Serializer) -> None:
        serializer.save()
