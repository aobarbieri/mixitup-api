from django.http import HttpResponse, HttpResponseNotFound
from datetime import date

from django.shortcuts import render

drinks = [
    {
        "slug": "marguerita",
        "image": "drink.jpg",
        "author": "Amanda Mitzian",
        "date": date(2021, 7, 21),
        "title": "Original Marguerita",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam."
    },
    {
        "slug": "marguerita",
        "image": "drink.jpg",
        "author": "Amanda Mitzian",
        "date": date(2021, 7, 21),
        "title": "Original Marguerita",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam."
    }
]

# Create your views here.
# Views are either a function or a class


def index(req):
    return render(req, 'cocktails/index.html')


def drinks(req):
    return render(req, 'cocktails/all-drinks.html')


def drink_details(req, slug):
    return render(req, 'cocktails/drink-details.html')
