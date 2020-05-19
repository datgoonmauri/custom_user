from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse

from custom_user.settings import AUTH_USER_MODEL
from myuser.forms import RegistrationForm, LoginForm


@login_required
def index(request):
	user_model = AUTH_USER_MODEL
	return render(request, 'index.html', {"user_model": user_model})


def registration_view(request):
	html = 'register.html'
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(
				username=username,
				password=raw_password
			)
			login(request, account)
			return HttpResponseRedirect(
				request.GET.get(next, reverse('home'))
			)
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, html, context)


def loginview(request):
	html = 'login.html'
	context = {}
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(
				request,
				username=data['username'],
				password=data['password'],
			)
			if user:
				login(request, user)
				return HttpResponseRedirect(
					request.GET.get(next, reverse('home'))
				)
		else:
			context['login_form'] = form
	else:
		form = LoginForm()
		context['login_form'] = form
	return render(request, html, context)


def logoutview(request):
	logout(request)
	messages.info(request, "Logged out")
	return HttpResponseRedirect(reverse('home'))
