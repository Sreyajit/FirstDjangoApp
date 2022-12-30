from ast import Try
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Question
class Homepage(View):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context= {
        'latest_question_list':latest_question_list,
    }
    def get(self, request):
        return render(request, "polls/index.html", context=self.context)
class Detail(DetailView):
    def get(self, request, question_id):
        try:
            question=get_object_or_404(Question, pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question not found")
        return render(request,"polls/detail.html",{'question':question})
class Results(View):
    def get(self, request, question_id):
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)
class Vote(View):
    def get(self, request, question_id):
        return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
