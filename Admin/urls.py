from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
]