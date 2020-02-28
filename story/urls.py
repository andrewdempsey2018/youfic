from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("adventure/", views.adventure, name="adventure"),
    path("fantasy/", views.fantasy, name="fantasy"),
    path("mystery/", views.mystery, name="mystery"),
    path("scifi/", views.scifi, name="scifi"),
    path('read/', views.read, name='read'),
    path('submit/', views.submit, name='submit'),
]
