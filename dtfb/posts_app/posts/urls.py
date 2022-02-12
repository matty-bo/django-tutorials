from .views import PostsView
from django.urls import path

urlpatterns = [
    path('', PostsView.as_view(), name='home')
]