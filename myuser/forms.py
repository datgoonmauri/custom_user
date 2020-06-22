from django import forms


class LoginForm(forms.Form):
    username = forms.CharField( max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUser(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    display_name = forms.CharField(max_length=150)
    homepage = forms.URLField(required=False)
    age = forms.IntegerField(widget=forms.NumberInput())