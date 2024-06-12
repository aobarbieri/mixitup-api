from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('<slug:slug>', views.drink_details, name='drink-details'),
    path('drinks', views.drinks, name='all-drinks')
]
