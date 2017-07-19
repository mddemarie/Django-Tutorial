import datetime

from django.utils import timezone
from django.test import TestCase

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

