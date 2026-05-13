from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient, Instruction
from django.http import HttpResponse

def addRecipe(request):
    if(request.method == "POST"):
        recipe_name = request.POST.get("recipe_name")
        course_type = request.POST.get("course_type").lower()
        cooking_time = request.POST.get("cooking_time")
        selected_difficulty = request.POST.get("selected_difficulty").lower()
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


def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            return render(request, 'contact_us.html', {
                'error_message': 'Please fill in all fields.'
            })

        print(f"Contact from {name} ({email}): {message}")

        return render(request, 'contact_us.html', {
            'success_message': f"Thank you, {name}! Your message has been sent."
        })

    return render(request, 'contact_us.html')

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe_name         = request.POST.get('recipe_name')
        course_type         = request.POST.get('course_type').lower()
        cooking_time        = request.POST.get('cooking_time')
        selected_difficulty = request.POST.get('selected_difficulty').lower()
        recipe_img          = request.POST.get('recipe_img')
        ingredients         = request.POST.getlist('ingredients')
        instructions        = request.POST.getlist('instructions')
        Recipe.update_recipe(recipe_id, recipe_name, course_type, selected_difficulty, cooking_time, recipe_img, ingredients, instructions)
        request.session["recipeAdded"] = "Recipe was updated successfully"
        return redirect("home")
    return render(request, 'adminrecipedetails.html', {'recipe': recipe})

