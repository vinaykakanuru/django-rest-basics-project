from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    # returns Boolean value True/False
    def has_object_permission(self, request, view, obj):
        if obj.user:
            return request.user == obj.user
        return False