from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def detail(request, question_id):
    return HttpResponse('look up question: ' %question_id)

def results(request, question_id):
    response='look up question'
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse('look up votes: ' %question_id)