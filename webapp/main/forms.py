from django.forms import ModelForm

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the username'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the firstname'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Enter the email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Enter the password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Repeat the password'}))
    role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the role'}), initial='User')

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2", "role"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Enter the password'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class MovementForm(ModelForm):
    date = forms.DateInput()

    user_name = forms.ModelChoiceField(queryset=User.objects.all())
    rooms = forms.ModelMultipleChoiceField(
        queryset=Room.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    company = forms.ModelChoiceField(queryset=Company.objects.all())


    class Meta:
        widgets = {
            'date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                       }),
        }
        model = Movement
        fields = ["date", "user_name", "rooms", "company"]


class CompanyForm(ModelForm):
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the company name'}))


    class Meta:
        model = Company
        fields = ["company_name"]


class RoomForm(ModelForm):
    room_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the room name'}))


    class Meta:
        model = Room
        fields = ["room_name"]


class SectionForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the section name'}))
    leader = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Section
        fields = ["name", "leader"]

