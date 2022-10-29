from django.urls import path

from . import views

urlpatterns = [
    path('', views.pengirim),
    path('penerima/', views.penerima),
]
