from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect

from users.models import UserProfile


def users_view(request):

    users = UserProfile.objects.all()[:5]
    template = 'users/users.html'
    context = {'users': users}

    return render(request, template, context)
