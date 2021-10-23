from django.urls import path, include
from .views import SignupPageView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignupPageView.as_view(), name='signup'),
]