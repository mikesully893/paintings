from django.contrib import admin

from .models import Painting


class PaintingAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "price",)

admin.site.register(Painting, PaintingAdmin)
