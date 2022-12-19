from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class Response(View):
    def get(self, request):
        return HttpResponse("hello world")
# Create your views here.
