from django.test import TestCase
from django.contrib.auth.models import User
from model_bakery import baker

from blog.models import Post


class InitPosts(TestCase):
    def setUp(self):
        self.text = "<h1>test test</h1>"
        self.author = baker.make(User)

        self.related_posts = baker.prepare(
            Post, _quantity=4, text=self.text, author=self.author, image=""
        )

        self.post = baker.make(
            Post,
            make_m2m=True,
            text=self.text,
            related_posts=self.related_posts,
            image="",
        )

        self.other_posts = baker.make(Post, _quantity=30, text=self.text, image="")

        self.post_with_image = baker.make(
            Post, text=self.text, image="cover_images/pic.jpg"
        )
