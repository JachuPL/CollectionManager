from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(min_length=6, max_length=30, required=True, label="Nazwa użytkownika")
    first_name = forms.CharField(min_length=2, max_length=30, required=True, label="Imię")
    last_name = forms.CharField(min_length=2, max_length=50, required=True, label="Nazwisko")
    email = forms.EmailField(required=True, label="Email")
    password = forms.CharField(min_length=8, max_length=24, required=True, widget=forms.PasswordInput, label="Hasło")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
