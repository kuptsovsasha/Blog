from django.contrib import admin
from django.urls import path

from .views import HomeView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('lib/<slug>/', PostDetailView.as_view(), name='post_detail'),
]
