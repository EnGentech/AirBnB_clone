#!/usr/bin/python3
"""Testing users"""
import unittest
from models.review import Review

class TestUser(unittest.TestCase):
	"""This is test for user class"""
	user = Review()
	def test_user(self):
		"""testing user class"""
		self.assertTrue(Review())
	
	def test_attr(self):
		"""testing the attributes of test class"""
		self.assertTrue(self.user.email=='')
		self.assertTrue(self.user.password=='')
		self.assertTrue(self.user.first_name=='')
		self.assertTrue(self.user.last_name=='')
		#self.assertTrue(hasattr(self.user, "email"))
		#self.assertTrue(hasattr(self.user, "password"))
		#self.assertTrue(hasattr(self.user, "first_name"))
		#self.assertTrue(hasattr(self.user, "last_name"))

	def test_attr_type(self):
		"""testing the attributes of test class"""
		self.assertTrue(isinstance(self.user.password, str))
		self.assertTrue(isinstance(self.user.email, str))
		self.assertTrue(isinstance(self.user.first_name, str))
		self.assertTrue(isinstance(self.user.last_name, str))
