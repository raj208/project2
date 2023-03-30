from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def courses(request):
    return render(request, 'pages/courses.html')

def fees(request):
    return render(request, 'pages/fees.html')

def protfilio(request):
    return render(request, 'pages/protfilio.html')

def sidebar(request):
    return render(request, 'pages/sidebar.html')

