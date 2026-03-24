from rest_framework import permissions

class UserModify(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and (request.user.isAdmin or request.user.isStaff)