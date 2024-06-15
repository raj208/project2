
from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         return format_html(f"<img src= {object.photo.url} width = '40px' styles = 'border_radius:100px'")
    
#     thumbnail.short_description = "photo"
#     list_display = ("product_name ",)
#     list_display_links = ("product_name","thumbnail")


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
         return format_html(f"<img src= {object.photo.url} width = '40px' styles = 'border_radius:100px'")
    
    thumbnail.short_description = "photo"
    list_display = ("id" ,"product_name","thumbnail","price")
    list_display_links = ("product_name", "thumbnail")


admin.site.register(Product, ProductAdmin)
