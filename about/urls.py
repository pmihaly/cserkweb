from django.urls import path

from .views import Homepage, AboutUs, House

app_name = "about"

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("rolunk/", AboutUs.as_view(), name="about_us"),
    path("cserkeszhaz/", House.as_view(), name="house"),
]

