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
    user = User.objects.get(user=request.user.id)
    profile = UserProfile.objects.get(user=request.user.id)
    template = 'users/profile.html'
    context = {'profile': profile, 'user':user}
    return render(request, template, context)

# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             registered = True
#         else:
#             print user_form.errors, profile_form.errors
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#     template = "users/register.html"
#     context = {'user_form': user_form,
#                'profile_form': profile_form,
#                'registered': registered
#                }
#     return render(request, template, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login')
