from django.views.generic import ListView, CreateView, DetailView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"


class RecipeDetailView(DetailView):
    model = Recipe
