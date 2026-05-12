from django.shortcuts import render
from .models import Recipe

def all_recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'all_recipes.html', {'recipes': recipes})



