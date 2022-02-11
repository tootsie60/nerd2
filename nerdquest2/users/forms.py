from subprocess import HIGH_PRIORITY_CLASS
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))

    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))

    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Email..'}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password'}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..', 'class': 'password'}))

    # reCaptcha token
    token = forms.CharField(
        widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2'
                  )


class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Email..'}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.modelForm):
    address = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True,
                           widget=forms.HiddenInput())
    county = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    country = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    lattitude = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('address', 'town', 'county', 'post_code',
                  'country', 'longitude', 'lattitude')
