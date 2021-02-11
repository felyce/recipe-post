from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView,
    DeleteView
)

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = "/"
