from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class PostList(ListView):
    model = Post
    template_name = "blog/bejegyzes_list.html"
    queryset = Post.get_published().order_by("-updated_at")


class PostDetail(DetailView):
    model = Post
    template_name = "blog/bejegyzes_detail.html"
