from django.urls import path

from . import views

urlpatterns = [
    path("api", views.index),
    path('api2', views.api)
]
