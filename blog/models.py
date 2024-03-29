from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="Cím")
    text = RichTextField(verbose_name="Szöveg", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author", verbose_name="Író"
    )
    image = models.ImageField(
        upload_to="blog/cover_images/", verbose_name="Borítókép", blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Létrehozás dátuma"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Utolsó módosítás dátuma"
    )

    slug = models.SlugField(unique=True, verbose_name="Link cím")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().update(*args, **kwargs)


class Announcement(Post):
    published = models.BooleanField(default=True, verbose_name="Közzétett állapot")

    related = models.ManyToManyField(
        "self", symmetrical=True, verbose_name="Kapcsolódó bejegyzések", blank=True
    )

    class Meta:
        verbose_name = "Közlemény"
        verbose_name_plural = "Közlemények"

    def get_absolute_url(self):
        return reverse("blog:announcement-detail", kwargs={"slug": self.slug})

    def get_published():
        return Announcement.objects.filter(published=True)

    def get_other(self):
        return (
            Announcement.get_published()
            .order_by("-updated_at")
            .exclude(Q(slug=self.slug) | Q(related__slug=self.slug))[:9]
        )


class Event(Post):
    published = models.BooleanField(default=True, verbose_name="Közzétett állapot")

    start_date = models.DateTimeField(
        verbose_name="Kezdeti dátum és idő", default=timezone.now
    )
    end_date = models.DateTimeField(
        verbose_name="Befejezési dátum és idő", default=timezone.now
    )

    class Meta:
        verbose_name = "Esemény"
        verbose_name_plural = "Események"

    def get_absolute_url(self):
        return reverse("blog:event-detail", kwargs={"slug": self.slug})

    def get_published():
        return Event.objects.filter(published=True)


class Note(models.Model):
    post = models.ForeignKey(
        Post, verbose_name="Megjegyzés", on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name="Szöveg", blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Létrehozás dátuma"
    )

    def __str__(self):
        return f"{self.post.__str__()} {self.created_at}"

    def __unicode__(self):
        return f"{self.post.__str__()} {self.created_at}"

    class Meta:
        verbose_name = "Megjegyzés"
        verbose_name_plural = "Megjegyzések"
