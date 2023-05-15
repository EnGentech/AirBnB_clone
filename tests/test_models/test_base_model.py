#!/usr/bin/python3
"""This file defines unit test cases
for base_model module
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """cass definition for unit testing"""
    
    def setUp(self):
        """Setup for instance"""
        self.fst = BaseModel()
        self.sec = BaseModel()

    def test_ModuleDocString(self):
        """Test module docstring of BaseModel instance"""
        self.assertTrue(len(BaseModel.__doc__) > 10)

    def test_ClassDocString(self):
        """Test class docstring"""
        self.assertFalse(len(BaseModel.__class__.__name__) > 5)

    def test_UuidKey(self):
        """Test the validation of uuid"""
        self.assertNotEqual(self.fst.id, self.sec.id)
        self.assertIsInstance(self.fst.id, str)
        
    def test_objectType(self):
        """Test if object is type dictionary"""
        self.assertIsInstance(self.sec.to_dict(), dict)

    def test_instance_type(self):
        """tests what the instance type is"""
        self.assertEqual(str(self.sec),
                        "[BaseModel] ({}) {}".format(BaseModel().id,
                        BaseModel().__dict__))

if __name__ == '__main__':
    unittest.main()
