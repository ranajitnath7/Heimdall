from django import http
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('health', lambda req: http.HttpResponse(200)),
    path('admin/', admin.site.urls),
]
