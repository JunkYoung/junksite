from django.shortcuts import render
from django.utils import timezone
from .models import Question

def index(request):
    return render(request, 'index.html')

def question_list(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'question/question_list.html', {'questions': questions})