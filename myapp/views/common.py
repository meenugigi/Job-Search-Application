from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from ..models import WebUser, User






# Create your views here.
class SignUpView(TemplateView):
    template_name = 'registration/select_account_signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_employer:
            return redirect('employer:employerhome')
        else:
            return redirect('webuser:userhome')
    return render(request, 'home/home.html')
