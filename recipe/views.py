from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"


class RecipeDetailView(DetailView):
    model = Recipe


# 新規追加
class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"
