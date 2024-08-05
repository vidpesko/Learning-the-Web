# Python standard libraries

# Thrid party libraries
from django.urls import path

# Custom libraries
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),  # Question detail page
    path("<int:question_id>/results/", views.results, name="results"),  # Question results page
    path("<int:question_id>/vote/", views.vote, name="vote"),   # Vote for question
]
