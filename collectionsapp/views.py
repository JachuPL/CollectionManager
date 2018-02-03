from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *


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
					return redirect('/')    # redirect to index
				else:
					return render(request, 'collections/login.html', {'error_message': 'Twoje konto zostało zablokowane'})
			else:
				return render(request, 'collections/login.html', {'error_message': 'Podany login lub hasło są niepoprawne'})
	return render(request, 'collections/login.html')


def register(request):
	form = UserForm(request.POST or None)
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
				collections = Collection.objects.filter(user=request.user)
				return render(request, 'collections/index.html', {'collections': collections})
	context = {
		"form": form,
	}
	return render(request, 'collections/register.html', context)
