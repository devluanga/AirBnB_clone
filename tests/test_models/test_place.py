#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
"""Checking the Place class"""
def testpep8(self):
"""testing the codestyle"""
pepstylecode = pep8.StyleGuide(quiet=True)
path_user = 'models/place.py'
result = pepstylecode.check_files([path_user])
self.assertEqual(result.total_errors,0.
