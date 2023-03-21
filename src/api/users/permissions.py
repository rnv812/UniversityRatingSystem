from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    """Object-level permission to only allow get his own profile."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj == request.user
