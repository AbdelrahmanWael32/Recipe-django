from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home_view, name='home'), IS NO LONGER USED
    path('add', views.addRecipe, name="add_recipe"),
]