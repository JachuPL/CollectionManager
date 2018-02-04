from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from django.db.models import Q


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('collections:login')
    else:
        return redirect('/')


def login_user(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return redirect('/')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')  # redirect to index
                else:
                    return render(request, 'collections/login.html',
                                  {'error_message': 'Twoje konto zostało zablokowane'})
            else:
                return render(request, 'collections/login.html',
                              {'error_message': 'Podany login lub hasło są niepoprawne'})
    return render(request, 'collections/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('collections:index')

    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('collections:index')
    context = {
        "form": form,
    }
    return render(request, 'collections/register.html', context)


def index(request):
    collections = Collection.objects.all()
    query = request.GET.get("q")
    if query:
        collections = collections.filter(Q(name__icontains=query) | Q(desc__icontains=query) |
                                         Q(created__icontains=query)).distinct()
    return render(request, 'collections/index.html', {'collections': collections})


def detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    collection_items = CollectionValue.objects.filter(collection_id=collection_id)
    query = request.GET.get("q")
    if query:
        collection_items = collection_items.filter(Q(name__icontains=query) | Q(desc__icontains=query) |
                                                   Q(aggregate__icontains=query) | Q(added__icontains=query) |
                                                   Q(date__icontains=query)).distinct()
    context = {
        'collection': collection,
        'collection_items': collection_items
    }
    return render(request, 'collections/detail.html', context)


def create_collection(request):
    if not request.user.is_authenticated:
        return redirect('collections:login')
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            return redirect('collections:detail', collection_id=collection.pk)
    else:
        form = CollectionForm()
    return render(request, 'collections/create_collection.html', {"form": form})


def delete_collection(request, collection_id):
    if request.user.is_authenticated:
        collection = Collection.objects.get(pk=collection_id)
        if request.user == collection.user:
            collection.delete()
    return redirect("/")


def edit_collection(request, collection_id):
    if not request.user.is_authenticated:
        return redirect('collections:login')

    collection = get_object_or_404(Collection, pk=collection_id)
    if not request.user == collection.user:
        return redirect('collections:index')

    if request.method == "POST":
        form = CollectionForm(request.POST or None, instance=collection)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.save()
            return redirect('collections:detail', collection_id=collection.pk)
    else:
        form = CollectionForm(instance=collection)
    return render(request, 'collections/edit_collection.html', {"form": form})


def item(request, value_id):
    collection_value = get_object_or_404(CollectionValue, pk=value_id)
    context = {'value': collection_value}
    return render(request, 'collections/item.html', context)


def create_item(request, collection_id):
    if not request.user.is_authenticated:
        return redirect('collections:login')

    collection = get_object_or_404(Collection, pk=collection_id)
    if not request.user == collection.user:
        return redirect('collections:detail', collection_id=collection_id)

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            collection_item = form.save(commit=False)
            collection_item.collection_id = collection
            collection_item.save()
            return redirect('collections:item', value_id=collection_item.id)
    else:
        form = ItemForm()
    return render(request, 'collections/create_item.html', {"form": form})


def delete_item(request, value_id):
    if request.user.is_authenticated:
        collection_item = CollectionValue.objects.get(pk=value_id)
        if request.user == collection_item.collection_id:
            collection_id = collection_item.collection_id.pk
            collection_item.delete()
    return redirect("collections:detail", collection_id=collection_id)


def edit_item(request, value_id):
    collection_item = get_object_or_404(CollectionValue, pk=value_id)

    if not request.user.is_authenticated or not request.user == collection_item.collection_id.user:
        return redirect("collections:detail", collection_id=collection_item.collection_id.pk)

    if request.method == "POST":
        form = ItemForm(request.POST or None, instance=collection_item)
        if form.is_valid():
            collection_item = form.save(commit=False)
            collection_item.save()
            return redirect('collections:item', value_id=collection_item.pk)
    else:
        form = ItemForm(instance=collection_item)
    return render(request, 'collections/edit_item.html', {"form": form})
