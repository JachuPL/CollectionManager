from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    username = forms.CharField(min_length=6, max_length=30, required=True, label="Nazwa użytkownika")
    first_name = forms.CharField(min_length=2, max_length=30, required=True, label="Imię")
    last_name = forms.CharField(min_length=2, max_length=50, required=True, label="Nazwisko")
    email = forms.EmailField(required=True, label="Email")
    password = forms.CharField(min_length=8, max_length=24, required=True, widget=forms.PasswordInput, label="Hasło")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class CollectionForm(forms.ModelForm):
    name = forms.CharField(min_length=1, max_length=150, required=True, label="Nazwa kolekcji")
    desc = forms.CharField(min_length=1, max_length=900, required=True, label="Opis kolekcji", widget=forms.Textarea())

    class Meta:
        model = Collection
        fields = ('name', 'desc')


class ItemForm(forms.ModelForm):
    name = forms.CharField(min_length=1, max_length=150, required=True, label="Nazwa przedmiotu")
    desc = forms.CharField(min_length=1, max_length=1900, required=True, label="Opis przedmiotu", widget=forms.Textarea())
    aggregate = forms.CharField(min_length=1, max_length=150, required=True, label="Agregat")
    date = forms.CharField(label="Data utworzenia", required=True, widget=forms.TextInput(attrs={'placeholder':'rrrr-mm-dd'}))

    class Meta:
        model = CollectionValue
        fields = ('name', 'aggregate', 'date', 'desc')
