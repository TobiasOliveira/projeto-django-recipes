from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipes


def home(request):
    recipes = Recipes.objects.filter(is_published=True).order_by('-id')

    return render(request, "recipes/pages/home.html", context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipes.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')

    return render(request, "recipes/pages/home.html", context={
        'recipes': recipes,
    })


def recipes(request, id):
    return render(request, "recipes/pages/recipes-view.html", context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
