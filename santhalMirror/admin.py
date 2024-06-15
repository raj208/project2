from django.contrib import admin
from .models import Personalities  # Correct the spelling if this is intended
from django.utils.html import format_html


# Register your models here.
class PersonalitiesAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="40px" style="border-radius:100px;" />', obj.personPhoto.url)

    thumbnail.short_description = "Photo"
    list_display = ("id", "personFirstName", "thumbnail")
    list_display_links = ("personFirstName", "thumbnail")

admin.site.register(Personalities, PersonalitiesAdmin)
