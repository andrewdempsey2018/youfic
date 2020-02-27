from django.shortcuts import render
from django.http import HttpResponse

# Import the Story model for use
from .models import Story

def index(request):
    # Query the database and pull out a set of all the stories it contains
    stories = Story.objects.all()
    # Pass the set of stories to the 'index' template
    return render(request, 'story/index.html', { 'stories': stories })