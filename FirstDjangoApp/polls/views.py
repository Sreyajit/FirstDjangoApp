from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, DetailView
class Homepage(View):
    def get(self, request, question_id):
        return HttpResponse("You are looking at question %s." % question_id)
class Detail(DetailView):
    def get(self, request, question_id):
        return HttpResponse("You are looking at question %s." % question_id)
class Results(View):
    def get(self, request, question_id):
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)
class Vote(View):
    def get(self, request, question_id):
        return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
