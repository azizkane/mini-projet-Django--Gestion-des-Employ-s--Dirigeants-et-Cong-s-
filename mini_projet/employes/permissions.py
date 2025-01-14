from rest_framework import permissions

class EstDirigeant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Dirigeants').exists()
