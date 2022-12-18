from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render("hello world")
# Create your views here.
