from django import forms
from django.contrib.auth.models import User
from .models import ServiceDetail


class CreateAccountForm(forms.ModelForm):
    '''
    User Form for creating new account
    '''
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        required = ['username', 'email', 'password']


class LoginForm(forms.Form):
    '''
    Login Form
    '''
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    fields = ['username', 'password']

class AddServiceDetail(forms.ModelForm):
    '''
    Form for adding a service
    '''
    price = forms.IntegerField()
    class Meta:
        model = ServiceDetail
        fields = ['price','service']
        required = ['price','service']