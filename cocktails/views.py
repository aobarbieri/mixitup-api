from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# Views are either a function or a class


def index(req):
    return render(req, 'cocktails/index.html')


def drinks(req):
    return render(req, 'cocktails/all-drinks.html')


def drink_details(request):
    pass
