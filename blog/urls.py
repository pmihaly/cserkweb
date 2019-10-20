from django.urls import path

from .views import BejegyzesList, BejegyzesDetail, Homepage

app_name = "blog"

urlpatterns = [
    path("", BejegyzesList.as_view(), name="bejegyzesek-list"),
    path("<slug:slug>/", BejegyzesDetail.as_view(), name="bejegyzesek-detail"),
    path("", Homepage.as_view(), name="homepage"),
]

