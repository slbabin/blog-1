from django.shortcuts import render
from django.views import generic
from .models import BlogPost


class PostList(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_time')
    template_name = 'index.html'
    paginate_by = 6

