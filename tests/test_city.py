#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import unittest
import pep8
from models.place import City

from models.base_model import BaseModel
from models.city import City
class TestCity(unittest.TestCase):
"""Testing the City class"""
def testpep8(self):
"""testing the codestyle"""
pepstylecode = pep8.StyleGuide(quiet=True)
path_user = 'models/city.py'
result = pepstylecode.check_files([path_user])
self.assertEqual(result.total_errors,0.
