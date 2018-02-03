from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CollectionForm


def index(request):
    collections = Collection.objects.all()
    context = {'collections': collections}
    return render(request, 'collections/index.html', context)


def detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    collection_items = CollectionValue.objects.filter(collection_id=collection_id)
    context = {
        'collection': collection,
        'collection_items': collection_items
    }
    return render(request, 'collections/detail.html', context)


def item(request, value_id):
    collection_value = get_object_or_404(CollectionValue, pk=value_id)
    context = {'value': collection_value}
    return render(request, 'collections/item.html', context)

def create_collection(request):
    form = CollectionForm(request.POST or None)
    if form.is_valid():
        collection = form.save(commit=False)
        collection.save()
        return render(request, 'collections/detail.html', {'collection': collection})
    context = {
        "form": form,
    }
    return render(request, 'collections/create_collection.html', context)