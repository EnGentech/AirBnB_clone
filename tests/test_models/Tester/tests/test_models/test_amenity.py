#!/usr/bin/python3
"""Testing users"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
	"""This is test for user class"""
	user = Amenity()
	def test_Amenity(self):
		"""testing amenity class"""
		self.assertTrue(Amenity())
	
	def test_attr(self):
		"""testing the attributes of test class"""
		self.assertTrue(self.user.name=='')
