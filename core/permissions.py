from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if hasattr(request.user,'extension'):
            return bool(request.user.extension.is_teacher)
        return False
