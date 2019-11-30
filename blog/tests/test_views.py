from django.test import TestCase
from django.urls import reverse

from . import InitPosts


class TestAnnouncementViews(InitPosts):
    def test_announcement_list_view(self):
        res = self.client.get(reverse("blog:post-list"))

        self.assertContains(res, self.announcement.title, status_code=200)

    def test_announcement_list_view_with_image(self):
        res = self.client.get(reverse("blog:post-list"))

        self.assertContains(
            res, self.announcement_with_image.image.url, status_code=200
        )

    def test_announcement_detail_view(self):
        res = self.client.get(
            reverse("blog:announcement-detail", kwargs={"slug": self.announcement.slug})
        )

        self.assertContains(res, self.announcement.title, status_code=200)

    def test_announcement_detail_view_with_image(self):
        res = self.client.get(
            reverse(
                "blog:announcement-detail",
                kwargs={"slug": self.announcement_with_image.slug},
            )
        )

        self.assertContains(
            res, self.announcement_with_image.image.url, status_code=200
        )

    def test_announcement_note(self):
        res = self.client.get(
            reverse(
                "blog:announcement-detail",
                kwargs={"slug": self.announcement_with_note.slug},
            )
        )

        self.assertContains(res, self.announcement_note.text, status_code=200)

        irrevelant_res = self.client.get(
            reverse("blog:announcement-detail", kwargs={"slug": self.announcement.slug})
        )

        self.assertNotContains(
            irrevelant_res, self.announcement_note.text, status_code=200
        )


class TestEventViews(InitPosts):
    def test_event_list_view(self):
        res = self.client.get(reverse("blog:post-list"))
        self.assertContains(res, self.event.title, status_code=200)

    def test_event_list_view_with_image(self):
        res = self.client.get(reverse("blog:post-list"))

        self.assertContains(res, self.event_with_image.image.url, status_code=200)

    def test_event_detail_view(self):
        res = self.client.get(
            reverse("blog:event-detail", kwargs={"slug": self.event.slug})
        )

        self.assertContains(res, self.event.title, status_code=200)

    def test_event_detail_view_with_image(self):
        res = self.client.get(
            reverse("blog:event-detail", kwargs={"slug": self.event_with_image.slug})
        )

        self.assertContains(res, self.event_with_image.image.url, status_code=200)

    def test_event_note(self):
        res = self.client.get(
            reverse("blog:event-detail", kwargs={"slug": self.event_with_note.slug},)
        )

        self.assertContains(res, self.event_note.text, status_code=200)

        irrevelant_res = self.client.get(
            reverse("blog:event-detail", kwargs={"slug": self.event.slug})
        )

        self.assertNotContains(irrevelant_res, self.event_note.text, status_code=200)

