from django.http import HttpResponseRedirect
from django.shortcuts import render


def donate(request):
    form = NameForm()
    return render(request, "donate.html", {"form": form})


import stripe
from django.shortcuts import render
from django.conf import settings

from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET


def donate(request):
    key = settings.STRIPE_PUBLISHABLE
    return render(request, "donate.html", {"key": key})


def thanks(request):
    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=500,
            currency="EUR",
            description="Donation to YouFic",
            source=request.POST["stripeToken"],
        )
    return render(request, "thanks.html")

