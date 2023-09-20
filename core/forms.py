from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import BookAssigned


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = fields = ['username',  'email', 'password1', 'password2']


class BookAssignForm(forms.ModelForm):
	class Meta:
		model = BookAssigned
		fields = "__all__"
