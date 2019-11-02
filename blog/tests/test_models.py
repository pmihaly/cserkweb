from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from model_bakery import baker

from blog.models import Post


class PostTests(TestCase):
    def setUp(self):
        self.text = "<h1>test test</h1>"
        self.author = baker.make(User)

        self.related_posts = baker.prepare(
            Post, _quantity=4, text=self.text, author=self.author
        )

        self.post = baker.make(
            Post, make_m2m=True, text=self.text, related_posts=self.related_posts
        )

        self.other_posts = baker.make(Post, _quantity=30, text=self.text)

    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Post))

        self.assertEqual(self.post.__unicode__(), self.post.title)
        self.assertEqual(self.post.__str__(), self.post.title)

        self.assertEqual(self.post.slug, slugify(self.post.title))

    def test_update(self):
        updated_post, _ = Post.objects.update_or_create(
            title=self.post.title, defaults={"title": "yoyoyo"}
        )

        self.assertNotEqual(updated_post.slug, self.post.slug)
        self.assertEqual(self.post.slug, slugify(self.post.title))

    def test_get_absolute_url(self):
        absolute_url = reverse("blog:post-detail", kwargs={"slug": self.post.slug})
        self.assertEqual(self.post.get_absolute_url(), absolute_url)

    def test_recent_posts(self):
        recent_posts = Post.recent_posts(Post)

        self.assertEqual(len(recent_posts), 3)

        self.assertGreaterEqual(recent_posts[0].updated_at, recent_posts[1].updated_at)
        self.assertGreaterEqual(recent_posts[0].updated_at, recent_posts[2].updated_at)
        self.assertGreaterEqual(recent_posts[1].updated_at, recent_posts[2].updated_at)

    def test_other_posts(self):
        other_posts = self.post.other_posts()

        self.assertEqual(len(other_posts), 9)

        self.assertGreaterEqual(
            other_posts[0].updated_at, list(other_posts)[-1].updated_at
        )

        self.assertNotIn(self.post, other_posts)

        self.assertNotIn(self.related_posts, other_posts)
