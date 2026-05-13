from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Profile
from recipes.models import Recipe


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        email    = request.POST['email']
        password = request.POST['password']
        confirm  = request.POST['confirm_password']
        is_admin = request.POST.get('is_admin') == 'admin'

        if password != confirm:
            return render(request, 'Accounts/signup.html', {'error': "Passwords don't match", 'old_username': username, 'old_email': email})
        if len(password) < 6:
            return render(request, 'Accounts/signup.html', {'error': "Password too short", 'old_username': username, 'old_email': email})
        if User.objects.filter(username=username).exists():
            return render(request, 'Accounts/signup.html', {'error': "Username already taken", 'old_username': username, 'old_email': email})
        if User.objects.filter(email=email).exists():
            return render(request, 'Accounts/signup.html', {'error': "This email already exists", 'old_username': username, 'old_email': email})

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
        password          = request.POST['password']

        user = authenticate(request, username=username_or_email, password=password)
        if user is None:
            try:
                u    = User.objects.get(email=username_or_email)
                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Accounts/login.html', {'error': 'Wrong username or password'})

    return render(request, 'Accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'change_username':
            new_username = request.POST.get('new_username', '').strip()

            if not new_username:
                return render(request, 'Accounts/profile.html', {
                    'profile': profile,
                    'error': "Username cannot be empty.",
                    'open_form': 'username',   
                })
            if User.objects.filter(username=new_username).exclude(pk=request.user.pk).exists():
                return render(request, 'Accounts/profile.html', {
                    'profile': profile,
                    'error': "Username already taken.",
                    'open_form': 'username',
                })

            request.user.username = new_username
            request.user.save()
            return redirect('profile')

        if action == 'change_password':
            old_password = request.POST.get('old_password', '')
            new_password = request.POST.get('new_password', '')
            confirm_pass = request.POST.get('confirm_pass', '')

            if not request.user.check_password(old_password):
                return render(request, 'Accounts/profile.html', {
                    'profile': profile,
                    'error': "Current password is incorrect.",
                    'open_form': 'password',  
                })
            if new_password != confirm_pass:
                return render(request, 'Accounts/profile.html', {
                    'profile': profile,
                    'error': "Passwords do not match.",
                    'open_form': 'password',
                })
            if len(new_password) < 6:
                return render(request, 'Accounts/profile.html', {
                    'profile': profile,
                    'error': "Password must be at least 6 characters.",
                    'open_form': 'password',
                })

            request.user.set_password(new_password)
            request.user.save()
            login(request, request.user)   
            return redirect('profile')

    return render(request, 'Accounts/profile.html', {'profile': profile})


@login_required(login_url='login')
def avatar_update_view(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        profile = request.user.profile
        profile.avatar = request.FILES['avatar']
        profile.save()
        return JsonResponse({'url': profile.avatar.url})
    return JsonResponse({'error': 'No file provided'}, status=400)
@login_required
def toggle_favorite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    profile = request.user.profile
    
    if profile in recipe.favourited_by.all():
        recipe.favourited_by.remove(profile)
    else:
        recipe.favourited_by.add(profile)
    
    return redirect(request.META.get('HTTP_REFERER', 'all_recipes'))

@login_required
def favorites(request):
    profile = request.user.profile
    recipes = profile.favourite_recipes.all()
    return render(request, 'Accounts/favorites.html', {'recipes': recipes})
