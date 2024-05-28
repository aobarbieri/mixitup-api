from django.http import HttpResponse, HttpResponseNotFound
from datetime import date

from django.shortcuts import render

all_drinks = [
    {
        "slug": "orig-marguerita",
        "image": "drink.jpg",
        "author": "Amanda Mitzian",
        "date": date(2021, 7, 21),
        "title": "Original Marguerita",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam."
    },
    {
        "slug": "trad-marguerita",
        "image": "drink.jpg",
        "author": "Amanda Mitzian",
        "date": date(2021, 11, 10),
        "title": "Tradicional Marguerita",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem 
            quos atque dolor, necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam. 
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa unde asperiores laboriosam dolorem autem quos atque dolor, 
            necessitatibus, saepe molestias ipsam culpa minus veritatis alias molestiae esse vel iure nam."""
    }
] # type: ignore

def get_date(post):
    return post['date']

# Create your views here.
# Views are either a function or a class


def index(req):
    sorted_drinks = sorted(all_drinks, key=get_date)
    latest_drinks = sorted_drinks[-2:]
    return render(req, 'cocktails/index.html', {
        "posts": latest_drinks
    })


def drinks(req):
    return render(req, 'cocktails/all-drinks.html', {
        "post": all_drinks
    })


def drink_details(req, slug):
    identified_drink = next(post for post in all_drinks if post['slug'] == slug)
    return render(req, 'cocktails/drink-details.html', {
        "drink": identified_drink
    })
