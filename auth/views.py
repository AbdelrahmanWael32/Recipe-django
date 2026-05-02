from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm_password']
        is_admin = request.POST.get('is_admin') == 'admin'

        if password != confirm:
            return render(request, 'auth/signup.html', {'error': "Passwords don't match"})
        if len(password) < 6:
            return render(request, 'auth/signup.html', {'error': "Password too short"})
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/signup.html', {'error': "Username already taken"})
        if User.objects.filter(email=email).exists():
            return render(request, 'auth/signup.html', {'error': "This email already exist"})

        
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, is_admin=is_admin)

        login(request, user)
        return redirect('home')

    return render(request, 'auth/signup.html')


def login_view(request):
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
            return render(request, 'auth/login.html', {'error': 'Wrong username or password'})

    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'auth/index.html')
# Create your views here.
