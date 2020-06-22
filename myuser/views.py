from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from custom_user.settings import AUTH_USER_MODEL
from myuser.forms import CustomUser, LoginForm
from myuser.models import MyUser


def index(request):
    html = "index.html"
    content = AUTH_USER_MODEL
    if request.user.is_authenticated:
        return render(request, html, {"content": content})
    return redirect("login")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def register(request):
    if request.method == "POST":
        form = CustomUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                email=data['email']
            )
            add_user = MyUser.objects.last()
            add_user.set_password(raw_password=data['password'])
            add_user.save()
            login(request, add_user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))
        return render(request, "register.html", {"form": form})
    form = CustomUser()
    return render(request, "register.html", {"form": form})