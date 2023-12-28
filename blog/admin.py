from django.contrib import admin
from .models import Blog
from django.utils.html import format_html
# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         return format_html(f"<img src= {object.photo.url} width = '40px' styles = 'border_radius:100px'")
    
#     thumbnail.short_description = "photo"
#     list_display = ("product_name ",)
#     list_display_links = ("product_name","thumbnail")


class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
         return format_html(f"<img src= {object.photo.url} width = '40px' styles = 'border_radius:100px'")
    
    thumbnail.short_description = "photo"
    list_display = ("id" ,"blog_name","thumbnail")
    list_display_links = ("blog_name", "thumbnail")


admin.site.register(Blog, BlogAdmin)
