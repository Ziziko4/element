from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    # Дополнительные пути, если необходимо
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)