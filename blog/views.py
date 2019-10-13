from django.shortcuts import render
from .models import Bejegyzes
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class BejegyzesList(ListView):
    model = Bejegyzes
    context_object_name = "bejegyzes"
    template_name = "blog/bejegyzes_list"


class BejegyzesDetail(DetailView):
    model = Bejegyzes
    template_name = "blog/bejegyzes_detail.html"

