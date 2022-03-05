#!/usr/bin/python3
"""Unittest for base_model.py
"""
import unittest
import pycodestyle
from models import base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class that test BaseModel"""

    def test_doc(self):
        """Checking documentation of BaseModel"""
        module = len(base_model.__doc__)
        self.assertGreater(module, 0)
