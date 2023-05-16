#!/usr/bin/python3
"""Testing users"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
	"""This is test for place class"""
	place = Place()
	def test_place(self):
		"""testing place class"""
		self.assertTrue(Place())
	
	def test_attr(self):
		"""testing the attributes of place class"""
		self.assertFalse(self.place.city_id==None)
		self.assertFalse(self.place.user_id==None)
		self.assertFalse(self.place.name==None)
		self.assertFalse(self.place.description==None)
		self.assertFalse(self.place.number_rooms==None)
		self.assertFalse(self.place.number_bathrooms==None)
		self.assertFalse(self.place.max_guest==None)
		self.assertFalse(self.place.price_by_night==None)
		self.assertTrue(self.place.latitude!=None)
		self.assertTrue(self.place.longitude!=None)
		self.assertTrue(self.place.amenity_ids!=None)
