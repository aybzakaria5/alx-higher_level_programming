#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_ids(self):
        self.assertEqual(self.Base(), 1)
        self.assertEqual(self.Base(), 2)
        self.assertEqual(self.Base(25), 25)
        self.assertEqual(self.Base(), 4)

if __name__ == "__main__":
    unittest.main()

