from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True  # Read only
        else:
            return obj.is_owner(request.user)  # Only owners are granted permissions for unsafe methods
