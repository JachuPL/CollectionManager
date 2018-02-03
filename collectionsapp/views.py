from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.save()
            return render(request, 'collections/detail.html', {'collection': collection})
    else:
        form = CollectionForm()
    return render(request, 'collections/create_collection.html', {"form": form})


def delete_collection(request, collection_id):
    colletion = Collection.objects.get(pk=collection_id)
    colletion.delete()
    return redirect("/")

def edit_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    if request.method == "POST":
        form = CollectionForm(request.POST or None, instance=collection)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.save()
            return redirect('collections:detail', collection_id=collection.pk)
    else:
        form = CollectionForm(instance=collection)
    return render(request, 'collections/edit_collection.html', {"form": form})
