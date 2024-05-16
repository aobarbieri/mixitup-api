from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# Views are either a function or a class


def drink_details(request, drink):
    if drink == '0520':
        return HttpResponse("Drink 0502 found!")
    else:
        return HttpResponseNotFound("Drink not found!")
