from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        home_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(home_url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        home_url = reverse('recipes:itens', kwargs={'id': 1})
        self.assertEqual(home_url, '/recipes/1/')
