from django.contrib import admin
from . import models, forms

# Register your models here.


@admin.register(models.Bejegyzes)
class BejegyzesAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "updated_at"]
    search_fields = ["title", "text"]
    form = forms.BejegyzesForm

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, "author"):
            obj.author = request.user
        super().save_model(request, obj, form, change)

