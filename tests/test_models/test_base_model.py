#!/usr/bin/python3
"""Testing our base_model file"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
	"""This class helps us to test the methods in our BaseModel"""
	model = BaseModel()
	user = User()
	def test_BaseModel(self):
		"""Testing the existence of BaseModel class"""
		self.assertTrue(BaseModel())
	
	def test_attributes(self):
		"""testing our class attributes"""
		self.assertTrue(isinstance(self.model.id, str))
		self.assertTrue(hasattr(self.model, "id"))
		self.assertTrue(hasattr(self.model, "created_at"))
		self.assertTrue(hasattr(self.model, "updated_at"))

	def test_methods(self):
		"""testing our class attributes"""
		self.assertTrue(hasattr(self.model, "save"))
		self.assertTrue(hasattr(self.model, "__str__"))
		self.assertTrue(hasattr(self.model, "__init__"))
		self.assertTrue(hasattr(self.model, "to_dict"))

	def test_str(self):
		"""testing the properties of __str__"""

	def test_unique_created_and_updated_datetime(self):
		"""testing our class attributes"""
		self.assertTrue(self.model.created_at != self.model.updated_at)

	def test_user(self):
		"""testing user class"""
		self.assertTrue(User())

	def test_place(self):
		"""testing user class"""
		self.assertTrue(Place())

	def test_city(self):
		"""testing user class"""
		self.assertTrue(City())

	def test_state(self):
		"""testing user class"""
		self.assertTrue(State())

	def test_review(self):
		"""testing user class"""
		self.assertTrue(Review())

	def test_amenity(self):
		"""testing user class"""
		self.assertTrue(Amenity())

	def test_module_docstring(self):
		"""lets test if we documented our module"""
		self.assertTrue(len(BaseModel.__doc__) >= 1)

	def test_class_docstring(self):
		"""lets test if we documented our module"""
		self.assertTrue(len(BaseModel.save.__doc__) >= 1)

	def tearDown(self):
		"""this runs after every method test finishes"""
		#print("A method just finished running. Tearing Down....")



