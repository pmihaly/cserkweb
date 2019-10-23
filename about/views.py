from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class Homepage(TemplateView):
    template_name = "about/homepage.html"


class AboutUs(TemplateView):
    template_name = "about/about_us.html"
