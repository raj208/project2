from django.urls import path
# from .views import login, register, dashboard, logout
from .views import login, register, dashboard, logout
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
]