from django.shortcuts import render
from .models import Bejegyzes
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

# Create your views here.


class BejegyzesList(ListView):
    model = Bejegyzes
    template_name = "blog/bejegyzes_list"


class BejegyzesDetail(DetailView):
    model = Bejegyzes
    template_name = "blog/bejegyzes_detail.html"


class Homepage(TemplateView):
    template_name = "about/homepage.html"
