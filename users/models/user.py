from django.contrib.auth.models import AbstractUser
from django.db import models

from users.models.location import Location


class User(AbstractUser):

    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Админ'
        MODERATOR = 'moderator', 'Модератор'
        MEMBER = 'member', 'Пользователь'

    role = models.CharField(max_length=200, choices=Roles.choices, default='member')
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["username"]

    def __str__(self):
        return self.username
