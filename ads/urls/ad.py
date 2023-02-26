from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.views.ad import AdUploadImageView, AdViewSet

ad_router = SimpleRouter()
ad_router.register('', AdViewSet)

urlpatterns = [
    path('<int:pk>/upload_image/', AdUploadImageView.as_view(), name='ad_upload_image'),
]

urlpatterns += ad_router.urls
