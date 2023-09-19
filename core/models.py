from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class BookDetail(models.Model):
	# username = models.ForeignKey(User, on_delete=models.CASCADE)
	book_name = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	price = models.IntegerField()
	available = models.BooleanField(default=True)
	tag1 = models.CharField(max_length=50)
	tag2 = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.book_name} by {self.author}"


class BookAssigned(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	book_name = models.ForeignKey(BookDetail, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.username} has {self.book_name}"


class Rating(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	book_name = models.ForeignKey(BookDetail, on_delete=models.CASCADE)
	rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

	def __str__(self):
		return f"{self.username} rates {self.book_name} as {self.rating}/10"
