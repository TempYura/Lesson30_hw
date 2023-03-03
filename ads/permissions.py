from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):
    message = "Редактировать/удалять может только создатель подборки/объявления."

    def has_object_permission(self, request, view, obj):
        if request.user == (obj.owner or obj.author):
            return True


class IsStaff(BasePermission):
    message = "Редактировать/удалять может только создатель объявления или модератор."

    def has_permission(self, request, view):
        if request.user.role in [User.Roles.MODERATOR, User.Roles.ADMIN]:
            return True
