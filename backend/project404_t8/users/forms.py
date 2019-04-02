from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    github_id = forms.CharField(required=False)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'displayname', 'email', 'github_id', 'github_url')
        labels = {
            'displayname': 'Display name',
            'github_id': 'Github Username',
            'github_url': 'Github URL'
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'password'}),
            
        }

