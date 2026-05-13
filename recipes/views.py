from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.http import HttpResponse

def addRecipe(request):
    if(request.method == "POST"):
        recipe_name = request.POST.get("recipe_name")
        course_type = request.POST.get("course_type")
        cooking_time = request.POST.get("cooking_time")
        selected_difficulty = request.POST.get("selected_difficulty")
        recipe_img = request.POST.get("recipe_img")
        ingredients = request.POST.getlist('ingredients')
        instructions = request.POST.getlist('instructions')

        Recipe.create_recipe(recipe_name, course_type, selected_difficulty, cooking_time, recipe_img, ingredients, instructions)

        
        return HttpResponse("Recipe added Successfully!!! (This should be the admin dashboard)")
        # pop the "recipe added successfully in admin_dashboard views.py"
        request.session["recipeAdded"] = ('Recipe was added successfully')
        return redirect("admin_dashboard")
    
    return render(request, "add_Recipe.html")
# Create your views here.


def all_recipes_view(request):
    query = request.GET.get('search', '')
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(Q(name__icontains=query) |
                                 Q(course_type__icontains=query) |
                                 Q(difficulty__icontains=query) |
                                 Q(ingredients__text__icontains=query)).distinct()
    return render(request, 'all_recipes.html', {'recipes': recipes, "query": query })



def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return render(request, 'recipe_detail.html', {'error': 'Recipe not found'})
    return render(request, 'recipe_detail.html', {'recipe': recipe})