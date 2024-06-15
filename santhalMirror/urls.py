from dajngo.urls import path
from .import views

urlpattern = [
    path('', views.home, name = "personalities")
]