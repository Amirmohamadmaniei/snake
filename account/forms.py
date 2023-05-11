from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if not user:
            raise ValidationError('username or password is wrong')

        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()

        if user:
            raise ValidationError('username is exists')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if len(password) < 8:
            raise forms.ValidationError('password more than 8 character')

        if password != password2:
            raise forms.ValidationError('password is not match')

        return self.cleaned_data
