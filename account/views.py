from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
from .models import User
from .mixins import NotLoginMixin


class RegisterView(NotLoginMixin, View):
    form_class = RegisterForm

    def get(self, request):
        return render(request, 'account/register.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            login(request, user)
            return redirect('home:home')
        return render(request, 'account/register.html', {'form': form})


class LoginView(NotLoginMixin, View):
    form_class = LoginForm

    def get(self, request):
        return render(request, 'account/login.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.POST['username'])
            login(request, user)
            return redirect('home:home')
        return render(request, 'account/login.html', {'form': form})


class LogoutView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request):
        logout(request)
        return redirect('account:login')
