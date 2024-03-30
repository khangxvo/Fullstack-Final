from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # This class inherited from the UserCreationForm
    email = forms.EmailField()

    class Meta:
        """
        - Give listed name space for configuaration
        - Keep configuration in one space
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
