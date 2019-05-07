from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def logged_in_view(request, *args, **kwargs):
    return render(request, "logged_in.html", {})

def logged_out_view(request, *args, **kwargs):
    return render(request, "logged_out.html", {})
