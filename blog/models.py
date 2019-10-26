from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import Q
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="Cím")
    text = RichTextField(verbose_name="Szöveg")
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="author", verbose_name="Író"
    )
    image = models.ImageField(
        upload_to="blog/cover_images/", verbose_name="Borítókép", blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Létrehozás")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Utolsó módosítás")

    slug = models.SlugField(unique=True, verbose_name="Link cím")

    related_posts = models.ManyToManyField(
        "self", symmetrical=True, verbose_name="Kapcsolódó bejegyzések", blank=True
    )

    published = models.BooleanField(default=True, verbose_name="Közzétett")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Bejegyzés"
        verbose_name_plural = "Bejegyzések"

    # pylint: disable=no-method-argument
    def get_published():
        return Post.objects.filter(published=True)

    def recent_posts(self):
        return Post.get_published().order_by("-updated_at")[:3]

    def other_posts(self):
        return (
            Post.get_published()
            .order_by("-updated_at")
            .exclude(Q(slug=self.slug) | Q(related_posts__slug=self.slug))[:9]
        )

