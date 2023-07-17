#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest
import pep8
from models.user import User

class Review_testing(unittest.TestCase):
"""Checking the User Class"""
def testpep8(self):
"""testing the codestyle"""
pepstylecode = pep8.StyleGuide(quiet=True)
path_user = 'models/user.py'
result = pepstylecode.check_files([path_user])
self.assertEqual(result.total_errors, 0.
