from django.urls import path

from .views import BejegyzesList, BejegyzesDetail

urlpatterns = [
    path("", BejegyzesList.as_view(), name="bejegyzesek-list"),
    path("<slug:slug>/", BejegyzesDetail.as_view(), name="bejegyzesek-detail"),
]

