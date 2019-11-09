from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from model_bakery import baker

from blog.models import Announcement

from . import InitPosts


class TestModels(InitPosts):
    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Announcement))

        self.assertEqual(self.post.__unicode__(), self.post.title)
        self.assertEqual(self.post.__str__(), self.post.title)

        self.assertEqual(self.post.slug, slugify(self.post.title))

    def test_update(self):
        updated_post, _ = Announcement.objects.update_or_create(
            title=self.post.title, defaults={"title": "yoyoyo"}
        )

        self.assertNotEqual(updated_post.slug, self.post.slug)
        self.assertEqual(self.post.slug, slugify(self.post.title))

    def test_get_absolute_url(self):
        absolute_url = reverse(
            "blog:announcement-detail", kwargs={"slug": self.post.slug}
        )
        self.assertEqual(self.post.get_absolute_url(), absolute_url)

    def test_get_recent(self):
        get_recent = Announcement.get_recent(Announcement)

        self.assertEqual(len(get_recent), 3)

        self.assertGreaterEqual(get_recent[0].updated_at, get_recent[1].updated_at)
        self.assertGreaterEqual(get_recent[0].updated_at, get_recent[2].updated_at)
        self.assertGreaterEqual(get_recent[1].updated_at, get_recent[2].updated_at)

    def test_get_other(self):
        get_other = self.post.get_other()

        self.assertEqual(len(get_other), 9)

        self.assertGreaterEqual(get_other[0].updated_at, list(get_other)[-1].updated_at)

        self.assertNotIn(self.post, get_other)

        self.assertNotIn(self.related, get_other)
