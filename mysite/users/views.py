from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .forms import CustomUserForm


def registration(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "users/registration.html", {"form":form})

def login(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            login(request,form.get_user())

    return render(request, "users/login.html", {"form":form})
