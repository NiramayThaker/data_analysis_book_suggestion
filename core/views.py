from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
@login_required(login_url='login/')
def home(request):
	return render(request, 'core/index.html')


def sign_up(request):
	form = UserRegistrationForm()
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("home")

	context = {'form': form}
	return render(request, 'registration/signup.html', context=context)


def assign_book(request):
	

	return render(request, "book_assign.html")
