#!/usr/bin/python3
"""test module"""


import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    def test_ids(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(25)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 25)
        self.assertEqual(b4.id, 4)
if __name__ == "__main__":
    unittest.main()
