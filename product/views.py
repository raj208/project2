from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    # products = Product.object.all()

    # data = {
    #     'products' : products ,
    # }

    product = Product.objects.all()
    return render(request, 'product/home.html', {'product':product})