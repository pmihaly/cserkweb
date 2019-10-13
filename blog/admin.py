from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Bejegyzes)
class BejegyzesAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at", "slug"]
    search_fields = ["title", "text"]

