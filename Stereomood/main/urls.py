from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.index, name='home'),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('songs', views.songs, name='songs'),
    path('search', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include("App.urls")),
    path('MusicPlayer', views.MusicPlayer, name='MusicPlayer')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)