from django.test import TestCase
from django.contrib.auth.models import User
from model_bakery import baker

from blog.models import Announcement


class InitPosts(TestCase):
    def setUp(self):
        self.text = "<h1>test test</h1>"
        self.author = baker.make(User)

        self.related = baker.prepare(
            Announcement, _quantity=4, text=self.text, author=self.author, image=""
        )

        self.get_other = baker.make(
            Announcement, _quantity=30, text=self.text, image=""
        )

        self.post = baker.make(
            Announcement, make_m2m=True, text=self.text, related=self.related, image="",
        )

        self.post_with_image = baker.make(
            Announcement, text=self.text, image="cover_images/pic.jpg"
        )
