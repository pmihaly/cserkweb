from django.db import models

# Create your models here.


class Bejegyzes(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="Cím")
    text = models.TextField(verbose_name="Szöveg")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Létrehozás")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Utolsó módosítás")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Bejegyzés"
        verbose_name_plural = "Bejegyzések"
