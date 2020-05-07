from django.shortcuts import (
    render,
    reverse,
    HttpResponseRedirect,
    HttpResponse
    )
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipebox_v1.models import Recipe, Author

from recipebox_v1.forms import (
    AddAuthorForm,
    AddRecipeFormSuperUser,
    AddRecipeFormNormalUser,
    LoginForm
    )


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


@login_required
def add_recipe(request):
    html = 'recipeaddform.html'

    if request.method == 'POST':
        if request.user.is_staff:
            form = AddRecipeFormSuperUser(request.POST)
        else:
            form = AddRecipeFormNormalUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'] if request.user.is_staff else request.user.author,
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('index'))

    if request.user.is_staff:
        form = AddRecipeFormSuperUser()
    else:
        form = AddRecipeFormNormalUser()
    context = {'form': form}
    return render(request, html, context)


@login_required
def add_author(request):
    html = 'authoraddform.html'

    if not request.user.is_staff:
        return HttpResponse(
            '<a href="/"> Home <a/>'
            '<br>'
            'Access Denied'
            )
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['name'],
                password='TempPassword1'
            )
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=user
            )
        return HttpResponseRedirect(reverse('index'))

    form = AddAuthorForm()
    context = {'form': form}
    return render(request, html, context)


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('index'))
                )
    form = LoginForm()
    return render(request, 'loginform.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


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
