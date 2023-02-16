from django.urls import path
from ads.views.cat import CategoryDetailView, CatListCreateView

urlpatterns = [
    path('', CatListCreateView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view()),
]
