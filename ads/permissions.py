from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):
    message = "Редактировать/удалять может только создатель подборки/объявления."

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "owner"):
            if request.user == obj.owner:
                return True
            return False
        if hasattr(obj, "author"):
            if request.user == obj.author:
                return True
            return False


class IsStaff(BasePermission):
    message = "Редактировать/удалять может только создатель объявления или модератор."

    def has_permission(self, request, view):
        if request.user.role in [User.Roles.MODERATOR, User.Roles.ADMIN]:
            return True
