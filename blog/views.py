from itertools import chain

from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Announcement, Event

# Create your views here.


class PostList(ListView):
    template_name = "blog/post_list.html"
    paginate_by = 9

    def get_queryset(self):
        return list(
            chain(
                Announcement.get_published().order_by("-updated_at"),
                Event.get_published().order_by("-updated_at"),
            )
        )


class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):

        context = super(AnnouncementDetail, self).get_context_data(**kwargs)
        context["domain_name"] = (
            "https://"
            if self.request.is_secure()
            else "http://" + self.request.get_host()
        )

        return context


class EventDetail(DetailView):
    model = Event
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):

        context = super(EventDetail, self).get_context_data(**kwargs)
        context["domain_name"] = (
            "https://"
            if self.request.is_secure()
            else "http://" + self.request.get_host()
        )
        context["event"] = True

        return context
