from django.urls import path
from ads.views.ad import AdListCreateView, AdDetailedView

urlpatterns = [
    path('', AdListCreateView.as_view()),
    path('<int:pk>', AdDetailedView.as_view()),
]
