"""
URL configuration for Web_BackEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home', permanent=True)), # REDIRECT FROM NOTHING/EMPTY URL TO HOME PAGE!!!
    path('home/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('Accounts/', include('Accounts.urls')),
    path('recipes/', include('recipes.urls')),
    path('Admin/', include('Admin.urls')),  # admin urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
