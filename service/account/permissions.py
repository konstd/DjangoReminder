from rest_framework import permissions


class AccountPermission(permissions.BasePermission):

    SAFE_METHODS = (
        'GET',
        'HEAD',
        'OPTIONS',
        'POST',
    )

    def has_object_permission(self, request, view, obj):
        if request.method in self.SAFE_METHODS:
            return True

        return request.user.id == obj.id
