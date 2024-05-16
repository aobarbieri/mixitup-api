from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views are either a function or a class


def index(request):
    return HttpResponse("This works!")


def api(request):
    return HttpResponse("We are on api 2!")
