from django.db import models

from users.models.location import Location


class User(models.Model):

    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Админ'
        MODERATOR = 'moderator', 'Модератор'
        MEMBER = 'member', 'Пользователь'

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=Roles.choices, default='member')
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["username"]

    def __str__(self):
        return self.username
