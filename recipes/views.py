from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from recipes.models import Recipes
from django.db.models import Q
from utils.pagination import make_pagination
import os

PER_PAGE = os.environ.get("PER_PAGE", 3)


def home(request):
    recipes = Recipes.objects.filter(
        is_published=True,
    ).order_by('-id')

    pagination_range, page_obj = make_pagination(
        request, recipes, PER_PAGE)

    return render(request, "recipes/pages/home.html", context={
        'recipes': page_obj,
        'pagination_range': pagination_range
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipes.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    pagination_range, page_obj = make_pagination(
        request, recipes, PER_PAGE)

    return render(request, "recipes/pages/home.html", context={
        'recipes': page_obj,
        'pagination_range': pagination_range
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


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipes.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    pagination_range, page_obj = make_pagination(
        request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', context={
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={ search_term }'
    })
