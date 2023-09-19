from django.shortcuts import render, HttpResponse
from .forms import UserRegistrationForm


# Create your views here.
def home(request):
	return render(request, 'core/index.html')


def sign_up(request):
	form = UserRegistrationForm()

	context = {'form': form}
	return render(request, 'registration/signup.html', context=context)
