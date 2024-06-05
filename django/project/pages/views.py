from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    #return HttpResponse ('Hello, World')
    x = {'name':'kkk', 'age':25}
    return render (request, 'pages/index.html', x)
def about (request):
    #return HttpResponse ('about, pages')
    return render (request, 'pages/about.html')
