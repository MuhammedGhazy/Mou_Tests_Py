from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import Loginform

def index (request):
    return render(request, 'pages/index.html')


def about(request):
    if request.method == 'POST' :
        dataform = Loginform(request.POST)
        if dataform.is_valid:
            dataform.save() 
    return render(request, 'pages/about.html', {"lf": Loginform()})
