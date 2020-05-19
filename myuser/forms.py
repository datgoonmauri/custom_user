from django import forms
from django.contrib.auth.forms import UserCreationForm
from myuser.models import Account


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Required. Add a valid email")

	class Meta:
		model = Account
		fields = ("email", "username", "password", "display_name")


class LoginForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(widget=forms.PasswordInput)
