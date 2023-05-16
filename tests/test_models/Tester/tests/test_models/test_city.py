#!/usr/bin/python3
"""Testing users"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
	"""This is test for user class"""
	user = City()
	def test_city(self):
		"""testing city class"""
		self.assertTrue(City())
	
	def test_attr(self):
		"""testing the attributes of city class"""
		self.assertTrue(self.user.state_id=='')
		self.assertTrue(self.user.name=='')
		#self.assertTrue(hasattr(self.user, "email"))
		#self.assertTrue(hasattr(self.user, "password"))
		#self.assertTrue(hasattr(self.user, "first_name"))
		#self.assertTrue(hasattr(self.user, "last_name"))

	def test_attr_type(self):
		"""testing the attributes of test class"""
		self.assertTrue(isinstance(self.user.state_id, str))
		self.assertTrue(isinstance(self.user.name, str))
