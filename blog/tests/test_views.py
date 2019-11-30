from django.test import TestCase
from django.urls import reverse

from . import InitPosts


class TestViews(InitPosts):
    def test_announcement_list_view(self):
        url = reverse("blog:announcement-list")
        res = self.client.get(url)

        self.assertContains(res, self.announcement.title, status_code=200)

    def test_announcement_list_view_with_image(self):
        url = reverse("blog:announcement-list")
        res = self.client.get(url)

        self.assertContains(
            res, self.announcement_with_image.image.url, status_code=200
        )

    def test_announcement_detail_view(self):
        url = reverse(
            "blog:announcement-detail", kwargs={"slug": self.announcement.slug}
        )
        res = self.client.get(url)

        self.assertContains(res, self.announcement.title, status_code=200)

    def test_announcement_detail_view_with_image(self):
        url = reverse(
            "blog:announcement-detail", kwargs={"slug": self.announcement.slug}
        )
        res = self.client.get(url)

        self.assertContains(
            res, self.announcement_with_image.image.url, status_code=200
        )
