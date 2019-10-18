from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Bejegyzes(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="Cím")
    text = RichTextField(verbose_name="Szöveg")
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="author", verbose_name="Író"
    )
    image = models.ImageField(upload_to="blog/cover_images/", verbose_name="Borítókép")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Létrehozás")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Utolsó módosítás")

    slug = models.SlugField(unique=True, verbose_name="Link cím")

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
