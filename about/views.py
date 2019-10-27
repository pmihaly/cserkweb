from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from blog.models import Post

# Create your views here.


class Homepage(ListView):
    template_name = "about/homepage.html"
    queryset = Post.recent_posts


class AboutUs(TemplateView):
    template_name = "about/about_us.html"


class House(TemplateView):
    template_name = "about/house.html"


def handler404(request, exception):
    response = render(request, "errors/404.html", status=404)
    print(exception)
    return response


def handler500(request):
    response = render(request, "errors/500.html", status=500)
    return response
