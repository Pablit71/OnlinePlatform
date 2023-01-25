from rest_framework.permissions import BasePermission

from circuit.models import Staff


class ListPermissions(BasePermission):
    message = "No men"

    def has_permission(self, request, view):
        if request.user:
            return True
        return False
