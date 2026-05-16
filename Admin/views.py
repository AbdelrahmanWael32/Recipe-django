from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe


@login_required
def admin_dashboard(request):
    recipes = Recipe.objects.all()
    
    # show success message if recipe was just added
    recipe_added_msg = request.session.pop("recipeAdded", None)
    
    return render(request, 'admin_dashboard.html', {
        'recipes': recipes,
        'recipe_added_msg': recipe_added_msg
    })

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("Admin/admin_dashboard")
    return redirect("Admin/admin_dashboard")