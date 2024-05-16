from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# Views are either a function or a class


def drink_details(request, drink):
    if drink == '0520':
        return HttpResponse(f"Drink {drink} found!")
    else:
        return HttpResponseNotFound("Drink not found!")


def drink_by_number(request, drink):
    return HttpResponse(drink)
