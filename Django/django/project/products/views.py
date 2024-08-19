from django.shortcuts import render
from products.models import Product

# Create your views here.
def product (request):
    return render (request, 'products/product.html')

def products (request):
    pro =  Product.objects.all()
    x = {'pro': pro.filter(price__range= [10, 1000])}
    return render (request, 'products/products.html', x)