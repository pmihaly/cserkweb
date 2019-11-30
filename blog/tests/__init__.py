from django.test import TestCase
from django.contrib.auth.models import User
from model_bakery import baker

from blog.models import Announcement, Event, Note


class InitPosts(TestCase):

    text = "<h1>test test</h1>"
    author = baker.make(User)

    def setup_test_object_no_relation(self, model, **model_kwargs):

        test_object = baker.make(
            model, make_m2m=True, text=self.text, image="", **model_kwargs
        )

        object_with_note = baker.make(
            model, make_m2m=True, text=self.text, image="", **model_kwargs
        )

        note = baker.make(Note, post=object_with_note)

        # pylint: disable=unused-variable
        other_objects = baker.make(model, _quantity=30, text=self.text, image="")

        object_with_image = baker.make(
            model, text=self.text, image="cover_images/pic.jpg"
        )

        return (test_object, object_with_image, object_with_note, note)

    def setup_test_object_with_relation(self, model, **model_kwargs):

        related_objects = baker.prepare(
            model,
            _quantity=4,
            text=self.text,
            author=self.author,
            image="",
            **model_kwargs
        )

        return (
            *self.setup_test_object_no_relation(model, related=related_objects),
            related_objects,
        )

    def setUp(self):
        (
            self.announcement,
            self.announcement_with_image,
            self.announcement_with_note,
            self.announcement_note,
            self.related_announcements,
        ) = self.setup_test_object_with_relation(Announcement)

        (
            self.event,
            self.event_with_image,
            self.event_with_note,
            self.event_note,
        ) = self.setup_test_object_no_relation(Event)
