from django.contrib import admin
from .models import Category, Recipes


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
