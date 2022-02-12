from posts.models import Post
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class PostsView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'