from django.shortcuts import render, get_object_or_404
from .models import Blog



# Create your views here.
def home(request):
    blogs = Blog.objects.all()

    data = {
        'blogs' : blogs ,
    }

    # product = Product.objects.all()
    return render(request, 'pages/fees.html', context =data)

def Blog_details(request, pk):
    blogs = get_object_or_404(Blog, id = pk)
    data = {
        'blog' : blogs,
    }
    return render(request, 'pages/blog_details.html', context=data)

# def Product_details(request):

#     return render(request, 'product/product_details.html')