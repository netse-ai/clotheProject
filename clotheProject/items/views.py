from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect

from items.models import Item


def item_view(request):

    items = Item.objects.all()
    template = 'items/items.html'
    context = {'items': items}

    return render(request, template, context)
