from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    teams = Team.objects.all()

    data = {
        'teams' : teams,
    }
    return render(request, 'pages/about.html', context=data)

def contact(request):
    return render(request, 'pages/contact.html')

def product(request):
    return render(request, 'pages/product.html')

def fees(request):
    return render(request, 'pages/fees.html')

def protfilio(request):
    return render(request, 'pages/protfilio.html')

def sidebar(request):
    return render(request, 'pages/sidebar.html')


