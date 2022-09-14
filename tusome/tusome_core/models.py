from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to=os.environ.get("IMAGE_URL"))
    upload_date = models.DateTimeField(timezone.now())
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='uploaded_books')
    slug = models.SlugField(max_length=250, unique_for_date='upload_date')
    

class Category(models.Model):
    name = models.CharField(max_length=100)
