from django.test import TestCase
from django.urls import reverse

from . import InitPosts


class TestViews(InitPosts):
    def test_post_list_view(self):
        url = reverse("blog:post-list")
        res = self.client.get(url)

        self.assertContains(res, self.post.title, status_code=200)

    def test_post_detail_view(self):
        url = reverse("blog:post-detail", kwargs={"slug": self.post.slug})
        res = self.client.get(url)

        self.assertContains(res, self.post.title, status_code=200)
