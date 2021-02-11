from django.views.generic import TemplateView
from django.views.generic import (
    CreateView, UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy

from django.contrib import messages

from recipe.models import Recipe


class StaffroomTemplateView(TemplateView):
    template_name = "staffroom/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['recipe_list'] = Recipe.objects.filter(user=self.request.user).prefetch_related("comment_set")
        else:
            context['recipe_list'] = None

        return context


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description", "image",]
    success_url = reverse_lazy("recipe:index")

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["title", "content", "description", "image", ]
    # success_url = "/"

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("recipe:detail", kwargs={"pk": pk})

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)
