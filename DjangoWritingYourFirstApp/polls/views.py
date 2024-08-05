from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


"""
In our poll application, we'll have the following four views:

    - Question “index” page - displays the latest few questions.
    - Question “detail” page - displays a question text, with no results but with a form to vote.
    - Question “results” page - displays results for a particular question.
    - Vote action - handles voting for a particular choice in a particular question.
"""

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]

    context = {
        "latest_question_list": latest_questions,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    response  = f"RESULTS {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    response = f"VOTING {question_id}"
    return HttpResponse(response)
