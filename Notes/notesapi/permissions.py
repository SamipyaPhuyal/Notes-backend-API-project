from rest_framework import permissions
 
class NoteModify(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.uploaded_by == request.user or (request.user.isAdmin or request.user.isStaff)
class LikePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return request.user.is_authenticated and (obj.liked_by != request.user)
        elif request.method == 'DELETE':
            return request.user.is_authenticated and (obj.liked_by == request.user)
class NoteCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True