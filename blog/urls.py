from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name = "blog"),
    # path('product_details/', views.Product_details, name ="product_details")
    path('blog/<int:pk>/', views.Blog_details, name = "Blog_details"),
] 



