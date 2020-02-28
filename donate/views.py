from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def donate(request):
    form = NameForm()
    return render(request, "donate.html", {'form': form})