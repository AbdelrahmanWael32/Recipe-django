from django.shortcuts import render

def home_view(request):
    return render(request, 'recipes/index.html')

# Create your views here.
