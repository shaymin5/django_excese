from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404, get_list_or_404


def index(request):
    questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions_list': questions_list}
    return render(request=request, template_name='polls/index.html', context=context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request=request, template_name='polls/detail.html', context=context)

def results(request, question_id):
    choice = get_list_or_404(Choice, question_id=question_id)
    choice.sort(key=lambda x: x.votes, reverse=True)
    question = get_object_or_404(Question, pk=question_id)
    context = {'choice': choice, 'question':question}
    return render(request=request, template_name='polls/results.html', context=context)

def vote(request, question_id):
    return HttpResponse("你正在给问题 %s 投票。" % question_id)
