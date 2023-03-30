
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('about/', views.about, name ="about"),
    path('contact/', views.contact, name ="contact"),
    path('courses/', views.courses, name ="courses"),
    path('fees/', views.fees, name ="fees"),
    path('protfilio/', views.protfilio, name ="protfilio"),
    path('sidebar/', views.sidebar, name ="sidebar"),
]
