from django.shortcuts import render

from accounts.forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')