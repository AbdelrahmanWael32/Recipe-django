from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/<int:pk>/toggle/', views.toggle_favorite, name='toggle_favorite'),

]