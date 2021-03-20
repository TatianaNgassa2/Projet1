# Create your views here.
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import NewUserForm, RegisterUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse, reverse_lazy
from django.contrib import messages  # import messages
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .models import Etudiant


def homepage(request):
    # return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")
    return render(request=request, template_name="home.html")


# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("templates:home")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm
#     return render(request=request, template_name="register.html", context={"register_form": form})


# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             login(request, user)
#             return redirect("home")
#
#         else:
#             for msg in form.error_messages:
#                 print(form.error_messages[msg])
#
#             return render(request=request,
#                           template_name="register.html",
#                           context={"form": form})
#
#     form = UserCreationForm
#     return render(request=request,
#                   template_name="register.html",
#                   context={"form": form})
def login_request1(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("EquipementSportif:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


# Create your views here.
def register_request(request):
    if request.method == "POST":
        form =RegisterUserForm(request.POST)
        if form.is_valid():
            d=Etudiant(form['username'].value())
            d.save()
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("EquipementSportif:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login/")
