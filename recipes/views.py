from django.db.models import Q
from django.shortcuts import render
from .models import Recipe

def all_recipes_view(request):
    query = request.GET.get('search', '')
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(Q(name__icontains=query) |
                                 Q(course_type__icontains=query) |
                                 Q(difficulty__icontains=query))
    return render(request, 'all_recipes.html', {'recipes': recipes, "query": query })



