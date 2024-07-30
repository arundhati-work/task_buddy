from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_view(request):
    if request.method=="GET":
        form = AuthenticationForm()
        context = {
            "form":form
        }
        return render(request, "authmanager/login.html", context)
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        else:
            context = {
            "form":form
        }
        return render(request, "authmanager/login.html", context)