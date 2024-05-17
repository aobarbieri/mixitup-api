from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('drinks', views.drinks, name='drinks-page'),
    path('drinks/<slug:slug>', views.drink_details, name='drink-detail-page')


]
