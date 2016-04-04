from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from items.models import Item, Favorite


def item_view(request):
    items = Item.objects.all()
    context = {"items":items}
    template = 'items/items.html'
    return render(request, template, context)


@login_required
def favorite_item(request):
    fav, created = Favorite.objects.get_or_create(user=request.user)
    if request.method == "POST":
        id = request.POST['id']
        item = Item.objects.get(id=id)
        fav.items.add(item)
        fav.save()
        print fav
    return HttpResponse('hello')
    # if item_id:
    #     fav = Favorite.objects.get(user=request.user)
    #     if fav:
    #         fav.save()
    #         fav.items.add(item=int(item_id))
