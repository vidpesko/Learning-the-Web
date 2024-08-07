import datetime

from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for question whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for question whose pub_date is more than 1 day old
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return Ture for question whose pub_date is less than 1 day old
        """
        time = timezone.now() - datetime.timedelta(hours=22, seconds=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days, create_choice=True):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(question_text=question_text, pub_date=time)
    if create_choice:
        question.choice_set.create(choice_text="Choice 1.")
    return question


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no question exist, show appropriate message.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_questions(self):
        """
        Questions with pub_date in the past are displayed on the index page.
        """
        question = create_question("Past question?", -3)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_future_and_past_questions(self):
        """
        If both types of question exist, only display past question.
        """
        past_question = create_question("Past question?", -3)
        create_question("Future question?", 3)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [past_question])

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question("Past question 1.?", -3)
        question2 = create_question("Past question 2.?", -9)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question1, question2])

    def test_question_without_choices(self):
        """
        The question without choices should not be displayed.
        """
        create_question("Question with no choices?", -3, create_choice=False)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_question_with_choices(self):
        """
        The question with choices should be displayed.
        """
        question = create_question("Question with choices?", -3)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future returns a 404 not found
        """
        future_question = create_question("Future question", 5)
        url = reverse("polls:detail", args=(future_question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_questions(self):
        """
        The detail view of a question with a pub_date in the past displays the question's text
        """
        question = create_question("Past question", -5)
        url = reverse("polls:detail", args=(question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.question_text)