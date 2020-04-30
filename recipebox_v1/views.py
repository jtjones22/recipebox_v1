from django.shortcuts import render

from recipebox_v1.models import Recipe, Author


def index(request):
    items = Recipe.objects.all()
    return render(
        request,
        'index.html',
        {
            'recipes': items,
        }
    )


def recipes(request, item_id):
    recipe = Recipe.objects.get(id=item_id)
    context = {'data': recipe}
    return render(
        request,
        'recipe.html',
        context
    )


def authors(request, item_id):
    author = Author.objects.get(id=item_id)
    recipes = Recipe.objects.all()
    context = {'author': author, 'recipes': recipes}
    return render(
        request,
        'author.html',
        context
    )