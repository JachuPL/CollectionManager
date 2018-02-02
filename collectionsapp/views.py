from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import RequestContext
from .models import *


def index(request):
	collections = Collection.objects.all()
	context = {'collections': collections}
	return render(request, 'polls/index.html', context)


def detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    collection_items = CollectionValue.objects.filter(collection_id=collection_id)
    context = {
        'collection': collection,
        'collection_items': collection_items
    }
    return render(request, 'polls/detail.html', context)


def item(request, value_id):
    collection_value = get_object_or_404(CollectionValue, pk=value_id)
    context = {'value': collection_value}
    return render(request, 'polls/item.html', context)
