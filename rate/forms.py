from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

# The rest of your forms remain the same
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'name']

class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['user', 'name']

class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = '__all__'
        exclude = ['user', 'name']

class Alert1Form(ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
        exclude = ['user', 'name']

class Alert2Form(ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
        exclude = ['user', 'name']

class AlertForm(ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
        exclude = ['user', 'name']

class PinForm(ModelForm):
    class Meta:
        model = Pin
        fields = '__all__'
        exclude = ['user', 'name']

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['user', 'name']
