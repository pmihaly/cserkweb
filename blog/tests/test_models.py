from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from model_bakery import baker

from blog.models import Announcement, Event, Note

from . import InitPosts


class TestAnncouncement(InitPosts):
    def test_creation(self):
        self.assertTrue(isinstance(self.announcement, Announcement))

        self.assertEqual(self.announcement.__unicode__(), self.announcement.title)
        self.assertEqual(self.announcement.__str__(), self.announcement.title)

        self.assertEqual(self.announcement.slug, slugify(self.announcement.title))

    def test_update(self):
        updated_announcement, _ = Announcement.objects.update_or_create(
            title=self.announcement.title, defaults={"title": "yoyoyo"}
        )

        self.assertNotEqual(updated_announcement.slug, self.announcement.slug)
        self.assertEqual(self.announcement.slug, slugify(self.announcement.title))

    def test_get_absolute_url(self):
        absolute_url = reverse(
            "blog:announcement-detail", kwargs={"slug": self.announcement.slug}
        )
        self.assertEqual(self.announcement.get_absolute_url(), absolute_url)

    def test_get_other(self):
        get_other = self.announcement.get_other()

        self.assertEqual(len(get_other), 9)

        self.assertGreaterEqual(get_other[0].updated_at, list(get_other)[-1].updated_at)

        self.assertNotIn(self.announcement, get_other)

        self.assertNotIn(self.related_announcements, get_other)


class TestEvent(InitPosts):
    def test_creation(self):
        self.assertTrue(isinstance(self.event, Event))

        self.assertEqual(self.event.__unicode__(), self.event.title)
        self.assertEqual(self.event.__str__(), self.event.title)

        self.assertEqual(self.event.slug, slugify(self.event.title))

    def test_update(self):
        updated_event, _ = Event.objects.update_or_create(
            title=self.event.title, defaults={"title": "yoyoyo"}
        )

        self.assertNotEqual(updated_event.slug, self.event.slug)
        self.assertEqual(self.event.slug, slugify(self.event.title))

    def test_get_absolute_url(self):
        absolute_url = reverse("blog:event-detail", kwargs={"slug": self.event.slug})
        self.assertEqual(self.event.get_absolute_url(), absolute_url)


class TestNote(InitPosts):
    def test_creation(self):
        self.assertTrue(isinstance(self.announcement_note, Note))

        self.assertEqual(
            self.announcement_note.__str__(),
            self.announcement_with_note.title
            + " "
            + str(self.announcement_note.created_at),
        )

        self.assertEqual(
            self.announcement_note.__unicode__(),
            self.announcement_with_note.title
            + " "
            + str(self.announcement_note.created_at),
        )
