from rest_framework.permissions import BasePermission


class Permissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
