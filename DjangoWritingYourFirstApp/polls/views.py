from typing import Any

from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Question, Choice


"""
In our poll application, we'll have the following four views:

    - Question “index” page - displays the latest few questions.
    - Question “detail” page - displays a question text, with no results but with a form to vote.
    - Question “results” page - displays results for a particular question.
    - Vote action - handles voting for a particular choice in a particular question.
"""

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        """
        Return the last five published questions. Using get_queryset method instead of model attribute because of custom logic (return last five elements)
        Excluding all questions, set to be published in the future and all questions without choices.
        """
        return Question.objects.annotate(num_choices=Count("choice")).filter(pub_date__lte=timezone.now(), num_choices__gt=0).order_by("-pub_date")[:5]  # __lte means LESS THAT or EQUAL


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
    def get_queryset(self) -> QuerySet[Any]:
        """
        Excludes and questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except KeyError:
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You did not select a choice!"
        })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))
        