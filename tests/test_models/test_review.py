#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import unittest
import pep8
from models.review import Review

class Review_testing(unittest.TestCase):
"""Checking the Review Class"""
def testpep8(self):
"""testing the codestyle"""
pepstylecode = pep8.StyleGuide(quiet=True)
path_user = 'models/review.py'
result = pepstylecode.check_files([path_user])
self.assertEqual(result.total_errors, 0.
