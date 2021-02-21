from django.shortcuts import render,redirect
from django.contrib.auth import login as lg,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import CustomUserForm
from django.conf import settings


def registration(request):
    if request.user.is_authenticated:
        return redirect('ecommerce:order_list')
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "users/registration.html", {"form":form})

def login(request):
    if request.user.is_authenticated:
        return redirect('ecommerce:order_list')
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                lg(request,user)
                return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "users/login.html", {"form":form})

