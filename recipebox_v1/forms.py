from django import forms

from recipebox_v1.models import Author


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeFormSuperUser(forms.Form):
    title = forms.CharField(max_length=30)
    # queryset allows us to auto full the drop down with data we choose.
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)


class AddRecipeFormNormalUser(forms.Form):
    title = forms.CharField(max_length=30)
    # queryset allows us to auto full the drop down with data we choose.
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
