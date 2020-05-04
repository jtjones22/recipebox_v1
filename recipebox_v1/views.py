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
    recipes = Recipe.objects.filter(author=author)
    context = {'author': author, 'recipes': recipes}
    return render(
        request,
        'author.html',
        context
    )


# IF we want name in url
# def authors(request, item_author):
#     og_name = item_author
#     if '-' in item_author:
#         og_name = item_author.replace('-', ' ').title()
#     author = Author.objects.get(name=og_name)
#     recipes = Recipe.objects.filter(author=author)
#     context = {'author': author, 'recipes': recipes}
#     return render(
#         request,
#         'author.html',
#         context
#     )


# Put this in recipe.html
# <h4>
# Author:
# <a href="{% url 'author' data.author.url %}">{{ data.author }}
# </a>
# </h4>
