from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.awal),
    path('products/', include('products.urls')),
    path('information/', include('information.urls')),
    path('cooperation/', include('cooperation.urls')),
    path('jago/', include('jago.urls')),
]
