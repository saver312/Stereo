# Create your views here.
from django.shortcuts import render, redirect

# imported our models
from django.core.paginator import Paginator
from . models import Song

def index(request):
    return render(request, 'main/index.html')

def MusicPlayer(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "MusicPlayer.html", context)