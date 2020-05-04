"""recipebox_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from recipebox_v1.models import Author, Recipe
from recipebox_v1 import views

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recipe/<str:item_id>/', views.recipes, name='recipe'),
    path('author/<str:item_id>/', views.authors, name='author'),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),

]

# IF we want name in url
# path('author/<str:item_author>/', views.authors, name='author')
