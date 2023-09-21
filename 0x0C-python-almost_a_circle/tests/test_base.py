#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.Testcase):
    def test_ids(self):
        self.assertEqual(self.Base(), 1)

