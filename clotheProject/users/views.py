from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect

from users.models import UserProfile
from items.models import Favorite
from users.forms import UnfavoriteForm


def users_view(request):
    users = UserProfile.objects.all()[:5]
    template = 'users/users.html'
    context = {'users': users}
    return render(request, template, context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            print user
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/users/profile/')
            else:
                return HttpResponse('Your account is disabled. \
                Please contact Administration.')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login credentials.")
    else:
        return render(request, 'users/login.html')

@login_required
def user_profile(request):
    user = User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(user=user)
    favorites = user.favorite.items.all()
    print favorites
    if request.method == "PUT":
        print "put"
        form = UnfavoriteForm(request.PUT)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponseRedirect('/users/profile/')
    else:
        form = UnfavoriteForm()
        template = 'users/profile.html'
        context = {'profile': profile, 'user':user, 'favorites':favorites, 'form':form}
    return render(request, template, context)

# @login_required
# def unfavorite_item(request):
#     print request
#     template = 'users/profile.html'
#     fav = Favorite.objects.get(user=request.user)
#     if request.method == "PUT":
#         print "put"
#         # id = request.POST['id']
#         # item = Item.objects.get(id=id)
#         # fav.items.remove(item)
#         # fav.save()
#         # print fav
#         form = UnfavoriteForm(request.PUT)
#         if form.is_valid():
#             print form.cleaned_data
#             return HttpResponseRedirect('/users/profile/')
#     else:
#         form = UnfavoriteForm()
#     return render(request, template, {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login')
