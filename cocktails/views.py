from django.shortcuts import render, get_object_or_404

from .models import Drink

# Create your views here.


def index(req):
    drinks = Drink.objects.all().order_by('date')
    # latest_drinks = drinks[-1:]

    return render(req, 'cocktails/index.html', {
        "drinks": drinks
    })


def drinks(req):
    drinks = Drink.objects.all()

    return render(req, 'cocktails/all-drinks.html', {
        "drinks": drinks
    })


def drink_details(req, slug):
    drink = get_object_or_404(Drink, slug=slug)

    return render(req, 'cocktails/drink-details.html', {
        "name": drink.name,
        "date": drink.date,
        "strength": drink.strength,
        "flavors": drink.flavors,
        "ingredients": drink.ingredients
    })
