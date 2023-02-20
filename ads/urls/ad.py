from django.urls import path
from ads.views.ad import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdUploadImageView

urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view(), name='ad_upload_image'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
]
