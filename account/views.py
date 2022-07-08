from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import UserCreationForm


class LogInView(LoginView):
    template_name='login.html'
    next_page = 'cut'


class SignUpView(CreateView):
    model = User
    template_name='signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
