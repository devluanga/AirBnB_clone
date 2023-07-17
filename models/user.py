#!/usr/bin/python3
"""Init for class User"""
from models.base_model import BaseModel

class User(BaseModel):
"""Implements the User class"""
first_name = ""
last_name = ""
email = ""
password = ""
