from django.test import TestCase


class TestRecipe(TestCase):

    def test_top_page(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_recipe_top(self):
        res = self.client.get("/recipe/")
        self.assertEqual(res.status_code, 200)