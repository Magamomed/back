from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from midterm2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
]+static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
