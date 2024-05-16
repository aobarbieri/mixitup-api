from django.urls import path

from . import views

urlpatterns = [
    path('<int:drink>', views.drink_by_number),
    path('<str:drink>', views.drink_details),
]
