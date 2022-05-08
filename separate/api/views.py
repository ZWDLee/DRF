from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Books
from rest_framework import viewsets
from api.serializers import UserSerializer, BooksSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer




