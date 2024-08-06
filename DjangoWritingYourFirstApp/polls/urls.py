# Python standard libraries

# Thrid party libraries
from django.urls import path

# Custom libraries
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # Question detail page
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # Question results page
    path("<int:question_id>/vote/", views.vote, name="vote"),   # Vote for question
]
