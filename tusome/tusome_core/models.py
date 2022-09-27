from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Category(models.Model):
    title = models.CharField(max_length=100)

class Book(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    #TODO: Get Cover from ISBN using Google Books API
    cover = models.ImageField(upload_to="uploads/")
    upload_date = models.DateTimeField(default = datetime.now())
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='uploaded_books')
    slug = models.SlugField(max_length=250, unique_for_date='upload_date')
    isbn = models.CharField(max_length=13)
    category = models.ManyToManyField(Category)

class Review(models.Model):
    options = (
        ('approved', 'Approved'),
        ('not_approved', 'Pending'),
        )

    class ReviewObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(approved='approved')

    class Meta:
        ordering = ('-written_date', )

    title = models.CharField(max_length=200)
    review_text = models.TextField(max_length=1500)
    review_writer = models.ForeignKey(User, on_delete=models.PROTECT)
    written_date = models.DateTimeField(default = datetime.now())
    book_title = models.ForeignKey(Book, related_name='reviews', on_delete=models.PROTECT)
    status = models.CharField(max_length=15, choices=options, default='not_approved')
    objects = models.Manager()
    reviewObjects = ReviewObjects()
