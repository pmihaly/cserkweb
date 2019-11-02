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

    def get_context_data(self, **kwargs):

        context = super(PostDetail, self).get_context_data(**kwargs)
        context["domain_name"] = (
            "https://"
            if self.request.is_secure()
            else "http://" + self.request.get_host()
        )

        return context
