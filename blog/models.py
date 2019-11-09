from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="Cím")
    text = RichTextField(verbose_name="Szöveg", blank=True, null=True)
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="author", verbose_name="Író"
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

    # pylint: disable=no-method-argument
    def get_published():
        return Announcement.objects.filter(published=True)

    def get_recent(self):
        return Announcement.get_published().order_by("-updated_at")[:3]

    def get_other(self):
        return (
            Announcement.get_published()
            .order_by("-updated_at")
            .exclude(Q(slug=self.slug) | Q(related__slug=self.slug))[:9]
        )
