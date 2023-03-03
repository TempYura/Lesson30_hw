from django.contrib import admin

from users.models import Location
from users.models import User


admin.site.register(User)
admin.site.register(Location)
