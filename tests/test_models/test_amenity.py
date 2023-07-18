#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import unittest
import pep8
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
"""checking the Amenity Class"""
def testpep8(self):
"""testing the codestyle"""
pepstylecode = pep8.StyleGuide(quiet=True)
path_user = 'models/amenity.py'
result = pepstylecode.check_files([path_user])
self.assertEqual(result.total_errors, 0.
