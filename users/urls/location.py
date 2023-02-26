from rest_framework.routers import SimpleRouter

from users.views.location import LocationViewSet

location_router = SimpleRouter()
location_router.register('location', LocationViewSet)
