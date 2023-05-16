#!/usr/bin/python3
"""Testing users"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
	"""This is test for user class"""
	user = State()
	def test_state(self):
		"""testing user class"""
		self.assertTrue(State())
	
	def test_attr(self):
		"""testing the attributes of test class"""
		self.assertTrue(self.user.name=='')
