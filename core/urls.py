from django.urls import path
from . import views


urlpatterns = [
	path("", views.home, name='home'),
	path('signup/', views.sign_up, name='sign-up'),
	path('assign-book/', views.assign_book, name='assign-book'),
]
