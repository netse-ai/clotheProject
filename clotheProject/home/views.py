from django.shortcuts import render

# Create your views here.

def home_view(request):
    template = "home/home.html"
    return render(request, template)
