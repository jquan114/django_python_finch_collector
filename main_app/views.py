from django.shortcuts import render
from .models import Finch

# Create your views here.


# define the home view

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finches = Finch.objects.all()
    return render(request, 'finch/index.html', {'finches':finches})
