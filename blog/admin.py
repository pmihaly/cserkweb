from django.contrib import admin
from . import models, forms

# Register your models here.


@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published", "created_at", "updated_at"]
    list_editable = ["published"]
    search_fields = ["title", "text"]
    form = forms.PostForm

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, "author"):
            obj.author = request.user
        super().save_model(request, obj, form, change)

