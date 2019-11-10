from django.urls import path

from .views import PostList, AnnouncementDetail, EventDetail

app_name = "blog"

urlpatterns = [
    path("", PostList.as_view(), name="announcement-list"),
    path(
        "kozlemeny/<slug:slug>/",
        AnnouncementDetail.as_view(),
        name="announcement-detail",
    ),
    path("esemeny/<slug:slug>/", EventDetail.as_view(), name="event-detail"),
]

