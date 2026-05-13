from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home_view, name='home'), IS NO LONGER USED
    path('add', views.addRecipe, name="add_recipe"),
    path('all_recipes/', views.all_recipes_view, name='all_recipes'),
    path("<int:pk>/", views.recipe_detail, name='recipe_detail'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),

]