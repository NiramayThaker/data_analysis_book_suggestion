from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookAssigned(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)

	# book_name = models.CharField(max_length=25)

	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
