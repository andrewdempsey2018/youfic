from django.shortcuts import render
from django.http import HttpResponse

# Import the Part model for use
#from .models import Part

def index(request):
    return render(request, 'index.html')