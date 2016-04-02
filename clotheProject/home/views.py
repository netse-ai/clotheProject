from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.shortcuts import render
from home.forms import UserForm
from users.models import UserProfile
# Create your views here.

def register(request):
    registered = False
    if request.method == "POST":
        print request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            UserProfile.objects.get_or_create(user=user)
            registered = True
            user = authenticate(username=username, password=password)
            if registered:
                login(request, user)
                return HttpResponseRedirect('/users/profile/')
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    template = "home/register.html"
    context = {'user_form':user_form}
    return render(request, template, context)
