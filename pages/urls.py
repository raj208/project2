
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('about/', views.about, name ="about"),
    path('contact/', views.contact, name ="contact"),
    path('product/', views.product, name ="product"),
    path('fees/', views.fees, name ="fees"),
    path('protfilio/', views.protfilio, name ="protfilio"),
    path('sidebar/', views.sidebar, name ="sidebar"),
]
