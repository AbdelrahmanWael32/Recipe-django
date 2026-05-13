from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from recipes.models import Recipe

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm_password']
        is_admin = request.POST.get('is_admin') == 'admin'

        if password != confirm:
            return render(request, 'Accounts/signup.html', {
                'error': "Passwords don't match",
                'old_username': username,
                'old_email': email, 
            })
        if len(password) < 6:
            return render(request, 'Accounts/signup.html', {
                'error': "Password too short",
                'old_username':username,
                'old_email':email})
        if User.objects.filter(username=username).exists():
            return render(request, 'Accounts/signup.html', {
                'error': "Username already taken",
                'old_username':username,
                'old_email':email})
        if User.objects.filter(email=email).exists():
            return render(request, 'Accounts/signup.html', {
                'error': "This email already exist",
                'old_username':username,
                'old_email':email})

        
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, is_admin=is_admin)

        login(request, user)
        return redirect('home')

    return render(request, 'Accounts/signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']

        user = authenticate(request, username=username_or_email, password=password)
        
        if user is None:
            try:
                u = User.objects.get(email=username_or_email)
                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Accounts/login.html', {'error': 'wrong username or password'})

    return render(request, 'Accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def toggle_favorite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    profile = request.user.profile
    
    if profile in recipe.favourited_by.all():
        recipe.favourited_by.remove(profile)
    else:
        recipe.favourited_by.add(profile)
    
    return redirect(request.META.get('HTTP_REFERER', 'all_recipes'))

# Create your views here.
@login_required
def favorites(request):
    profile = request.user.profile
    recipes = profile.favourite_recipes.all()
    return render(request, 'Accounts/favorites.html', {'recipes': recipes})

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
        return redirect("admin_dashboard")
    return redirect("admin_dashboard")