from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.forms import UserForm
# Create your views here.

def register(request):
    registered = False
    if request.method == "POST":
        pritn request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
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
