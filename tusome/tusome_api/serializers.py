from rest_framework import serializers
from tusome_core.models import Book, Review

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'author', 'cover')