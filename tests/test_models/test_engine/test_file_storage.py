#!/usr/bin/python3
"""Testing users"""
import unittest
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """This is test for user class"""
    user = FileStorage()

    def test_File_storage(self):
        """testing user class"""
        self.assertTrue(FileStorage())

    def test_objectType(self):
        """checking if the attribute __object exist"""
        self.assertTrue(hasattr(self.user, FileStorage.__objects))
        # self.assertTrue(hasattr(self.user.__file_path))

    def test_all(self):
        """checking if all method exist"""
        self.assertTrue(hasattr(self.user, "all"))

    def test_new(self):
        """checking if the method new exist"""
        self.assertTrue(hasattr(self.user, "new"))

    def test_save(self):
        """check for save method in file_storage"""
        self.assertTrue(hasattr(self.user, "save"))

    def test_reload(self):
        """check for the existence of reload in file_storage"""
        self.assertTrue(hasattr(self.user, "reload"))
