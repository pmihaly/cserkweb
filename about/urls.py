from django.urls import path

from .views import Homepage

app_name = "about"

urlpatterns = [path("", Homepage.as_view(), name="homepage")]

