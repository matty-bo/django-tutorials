from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def homePageView(request):
#     return render(request=request, template_name='home.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
