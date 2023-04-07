from django.shortcuts import render, get_object_or_404
from .models import Product



# Create your views here.
def home(request):
    products = Product.objects.all()

    data = {
        'products' : products ,
    }

    # product = Product.objects.all()
    return render(request, 'product/home.html', context =data)

def Product_details(request):
    # Product = get_object_or_404(Product, id = pk)
    # data = {
    #     'product' : Product
    # }
    return render(request, 'product/product_details.html')