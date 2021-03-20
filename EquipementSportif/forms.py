from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


# Create your forms here.
class RegisterUserForm(forms.ModelForm):
    nom = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'entrez votre nom'}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'entrez votre prenom'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'confirmation mot de passe'}))
   # Etablissement = forms.ChoiceField(Etablissement.objects.all())

    class Meta:
        model = User
        fields = ['username', 'nom','prenom','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'autofocus': True,'placeholder': 'entrez votre matricule'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'adresse électronique', 'required': True})
        }

    # Validating password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
#
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]
#
#         def __init__(self, *args, **kwargs):
#             super(RegisterForm, self).__init__(*args, **kwargs)
#             for field_name, field in self.fields.items():
#                 field.widget.attrs['class'] = 'form-input'


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'autofocus': True, 'placeholder': 'Nom d\' utilisateur'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'mot de passe'}))


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
