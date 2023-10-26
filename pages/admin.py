from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f"<img src= {object.photo.url} width = '40px' styles = 'border_radius:100px'")
    
    thumbnail.short_description = "photo"   
    list_display = ("id", "first_name", "designation","thumbnail")    #need more than 1 value or add , 
    list_display_links = ( "first_name","thumbnail")                         #(one element on it's on is not a tuple,
    search_fields = ("first_name", "designation")                   #there should be more than one element)
    list_filter = ("designation",)     
    ordering = ("id",)  #ordering = ("-id",) for reversing order


# class TeamAdmin(admin.ModelAdmin): 
#     list_display = ("id", "first_name", "designation")    #need more than 1 value or add , 
#     list_display_links = ( "first_name","designation")                         #(one element on it's on is not a tuple,
#     search_fields = ("first_name", "designation")                   #there should be more than one element)
#     list_filter = ("first_name","designation")     
#     ordering = ("id",)  #ordering = ("-id",) for reversing order

admin.site.register(Team, TeamAdmin)