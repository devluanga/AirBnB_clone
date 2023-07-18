#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import unittest
import pep8
from models.state import State

class State_testing(unittest.TestCase):
"""Checking the State Class"""
def testpep8(self):
"""testing the codestyle"""
pepstylecode = pep8.StyleGuide(quiet=True)
path_user = 'models/state.py'
result = pepstylecode.check_files([path_user])
self.assertEqual(result.total_errors, 0.
