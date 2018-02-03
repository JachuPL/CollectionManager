from django import forms
from .models import *


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ('name', 'desc')


class ItemForm(forms.ModelForm):

    class Meta:
        model = CollectionValue
        fields = ('name', 'aggregate', 'date', 'desc')