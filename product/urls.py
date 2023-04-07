from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name = "product"),
    # path('product_details/', views.Product_details, name ="product_details")
    path('product/<int:pk>/', views.Product_details, name = "product_details"),
] 

