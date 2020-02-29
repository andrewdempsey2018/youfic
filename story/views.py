from django.shortcuts import render
from django.http import HttpResponse

# Import the Story model for use
from .models import Story


def index(request):
    # Query the database and pull out a set of all the stories it contains
    stories = Story.objects.all()
    # Pass the set of stories to the 'index' template
    return render(request, "story/index.html", {"stories": stories})


def adventure(request):
    stories = Story.objects.filter(category="Adventure")
    return render(request, "story/index.html", {"stories": stories})


def fantasy(request):
    stories = Story.objects.filter(category="Fantasy")
    return render(request, "story/index.html", {"stories": stories})


def mystery(request):
    stories = Story.objects.filter(category="Mystery")
    return render(request, "story/index.html", {"stories": stories})


def scifi(request):
    stories = Story.objects.filter(category="SciFi")
    return render(request, "story/index.html", {"stories": stories})


def read(request):
    story = Story.objects.get(id=request.GET.get("id"))
    return render(request, "story/read.html", {"story": story})

def submit(request):
    if request.method == "POST":
        if request.POST.get("title") and request.POST.get("author") and request.POST.get("description") and request.POST.get("category") and request.POST.get("text"):
            story = Story()
            story.title = request.POST.get("title")
            story.author = request.POST.get("author")
            story.description = request.POST.get("description")
            story.category = request.POST.get("category")
            story.text = request.POST.get("text")
            story.save()

            return render(request, "index.html")

    else:
        return render(request, "story/submit.html")

