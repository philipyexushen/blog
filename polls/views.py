from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("fuck you")


def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")

