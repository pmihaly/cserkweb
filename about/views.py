from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from blog.models import Bejegyzes

# Create your views here.


class Homepage(ListView):
    template_name = "about/homepage.html"
    queryset = Bejegyzes.recent_posts


class AboutUs(TemplateView):
    template_name = "about/about_us.html"