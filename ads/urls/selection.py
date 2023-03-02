from rest_framework.routers import SimpleRouter
from ads.views.selection import SelectionViewSet


selection_router = SimpleRouter()
selection_router.register('', SelectionViewSet)

urlpatterns = selection_router.urls
