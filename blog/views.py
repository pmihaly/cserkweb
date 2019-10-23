from django.shortcuts import render
from .models import Bejegyzes
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class BejegyzesList(ListView):
    model = Bejegyzes
    template_name = "blog/bejegyzes_list.html"
    queryset = Bejegyzes.objects.order_by("-updated_at")


class BejegyzesDetail(DetailView):
    model = Bejegyzes
    template_name = "blog/bejegyzes_detail.html"
