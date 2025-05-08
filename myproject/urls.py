from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from myapp.views import error404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

handler404 = error404
