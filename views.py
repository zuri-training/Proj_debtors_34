from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from logapp.forms import CustomUserCreationForm

def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect( "settings.LOGIN_REDIRECT_URL")
    return render(request, 'signup.html', context={'form': form})
            #return redirect(reverse("dashboard"))
# Create your views here.
#def logapp(request):
   # return render(request, 'register.html', {})

#def dashboard(request):
    #return render(request, 'dashboard.html')