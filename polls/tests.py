import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question

class QuestionModelTest(TestCase):

	def test_was_published_recently_with_future_question(self):
		# setup
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		# call the method
		result = future_question.was_published_recently()
		# assert correct behavior
		self.assertIs(result, False)

	def test_was_published_recently_with_old_question(self):
		"""
		If the question is old, was_published_recently returns False.
		"""
		time = timezone.now() - datetime.timedelta(days=2)
		old_question = Question(pub_date=time)
		result = old_question.was_published_recently()
		self.assertIs(result, False)

	def test_was_published_recently_with_new_question(self):
		"""
		if the question is new, was_published_recently returns True.
		"""
		time = timezone.now() - datetime.timedelta(hours=5)
		new_question = Question(pub_date=time)
		result = new_question.was_published_recently()
		self.assertIs(result, True)

	def create_question(question_text, days):
		"""
		Create a question with the given 'question_text' and published the
		given number of 'days' offset to now (negative for questions published
		in the past, positive for questions that have yet to be published).
		"""
		time = timezone.now() + datetime.timedelta(days=days)
		return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
	def test_no_questions(self):
		"""
		If no questions exist, an appropriate message is displayed.
		"""
	response = self.client.get(reverse('polls:index'))
	self.assertEqual(response.status_code, 200)
	self.assertContains(response, "No polls are available.")
	self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_past_question(self):
		"""
		Questions with a pub_date in the past are displayed on the 
		index page.
		"""
		create_question(question_text="Past question.", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question.>']
			)

	def test_future_question(self):
		"""
		Questions with a pub_date in the future aren't displayed on
		the index page.
		"""
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_future_question_and_past_question(self):
		"""
		Even if both past and future questions exist, only past questions
		are displayed.
		"""
		create_question(question_text="Past question.", days=30)
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question.>']
			)

	def test_two_past_questions(self):
		"""
		The questions index page may display multiple questions.
		"""
		create_question(question_text="Past question 1.", days=-30)
		create_question(question_text="Past question 2.", days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question 2.>', '<Question: Past question 1.>'])
