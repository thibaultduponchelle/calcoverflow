from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
  username = forms.CharField(label="",max_length=140, widget=forms.TextInput(attrs={'class' : 'login-input'}))
  password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class' : 'login-input'}))

class RegisterForm(AuthenticationForm):
  title = forms.CharField(label="",max_length=140, widget=forms.TextInput(attrs={'class' : 'post-title'}))
  content = forms.CharField(label="", widget=forms.Textarea(attrs={'id' : 'markdown'}))
