from django.contrib import admin
from django.urls import path, include

# Я е?№*"Ь с питоном, мне норм

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('filter.urls')),
]
