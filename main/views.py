from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def index(respond):
    return HttpRequest("<h1>Hello World !</h1>")
