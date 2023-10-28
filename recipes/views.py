from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipes


def home(request):
    recipes = Recipes.objects.filter(
        is_published=True,
    ).order_by('-id')

    return render(request, "recipes/pages/home.html", context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipes.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, "recipes/pages/home.html", context={
        'recipes': recipes,
    })


def recipes(request, id):
    recipes = get_object_or_404(
        Recipes.objects.filter(
            pk=id,
            is_published=True,
        )
    )
    return render(request, "recipes/pages/recipes-view.html", context={
        'recipe': recipes,
        'is_detail_page': True,
    })
