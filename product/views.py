from django.shortcuts import render
from .models import Product
from .models import Product_details

# Create your views here.
def home(request):
    products = Product.objects.all()

    data = {
        'products' : products ,
    }

    product = Product.objects.all()
    return render(request, 'product/home.html', context =data)

def Product_details(request):
    return render(request, 'product/product_details.html')