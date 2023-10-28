from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView


def closes(request):
    return render(request, 'main_page.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authenticate/register_users.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'authenticate/login_users.html'

    def get_success_url(self):
        return reverse_lazy('closes')


def user_logout(request):
    logout(request)
    return redirect('closes')
