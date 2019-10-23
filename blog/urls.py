from django.urls import path

from .views import BejegyzesList, BejegyzesDetail

app_name = "blog"

urlpatterns = [
    path("", BejegyzesList.as_view(), name="post-list"),
    path("<slug:slug>/", BejegyzesDetail.as_view(), name="post-detail"),
]

