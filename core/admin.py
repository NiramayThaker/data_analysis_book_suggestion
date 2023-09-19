from django.contrib import admin
from .models import BookDetail, BookAssigned, Rating


# Register your models here.
admin.site.register(BookDetail)
admin.site.register(BookAssigned)
admin.site.register(Rating)
