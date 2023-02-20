from django.contrib import admin

from ads.models.ad import Ad
from ads.models.category import Category


admin.site.register(Ad)
admin.site.register(Category)
