from django.shortcuts import render
from django.core.paginator import Paginator




# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def songs(request):
    return render(request, 'main/songs.html')


def search(request):
    return render(request, 'main/search.html')


def login(request):
    return render(request, 'registration/login.html')


def MusicPlayer(request):
    return render(request, "MusicPlayer.html")