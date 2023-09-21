#!/usr/bin/python3
"""test module for rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """tests if the Rectangle is a subclass to Bse"""

    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    """testing with no args given"""
    def testWidthNoArg(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle()
    #Wisth-testing-----------------------------------------

    """testing the width is either float or stinrg"""
    def test_WidthFloat(self):
        with self.assertRaises(TypeError):
            rec2 = Rectangle(3.0, 20)
    def test_WidthString(self):
        with self.assertRaises(TypeError):
            rec2 = Rectangle("width", 20)

    """testing the setting methode for width"""
    def test_WidthsetNone(self):
        rec2 = Rectangle(13, 20)
        with self.assertRaises(TypeError):
            rec2.width =None
    
    def test_WidthSetNegative(self):
        rec2 = Rectangle(13, 20)
        with self.assertRaises(ValueError):
            rec2.width =-13
    
    def test_WidthSetFloat(self):
        rec2 = Rectangle(13, 20)
        with self.assertRaises(TypeError):
            rec2.width =13.0
    
    def test_WidthZero(self):
        with self.assertRaises(ValueError):
            rec1 = Rectangle(0, 5)

    def test_WidthSetZero(self):
        rec1 = Rectangle(7, 5)
        with self.assertRaises(ValueError):
            rec1.width = 0
    def test_WidthNormalCase(self):
        rec1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec1.width, 1)
            
    #height-testing-----------------------------------------

    """testing the hiehgt is either float or stinrg"""
    def test_HieghtFloat(self):
        with self.assertRaises(TypeError):
            rec2 = Rectangle(3, 2.0)
    def test_Heighttring(self):
        with self.assertRaises(TypeError):
            rec2 = Rectangle(20, "height")

    """testing the setting methode for height"""
    def test_heightsetNone(self):
        rec2 = Rectangle(13, 20)
        with self.assertRaises(TypeError):
            rec2.height =None
    
    def test_heightSetNegative(self):
        rec2 = Rectangle(13, 20)
        with self.assertRaises(ValueError):
            rec2.height =-13
    
    def test_HeightSetFloat(self):
        rec2 = Rectangle(13, 20)
        with self.assertRaises(TypeError):
            rec2.height =13.0
    
    def test_HieghtZero(self):
        with self.assertRaises(ValueError):
            rec1 = Rectangle(5, 0)

    def test_HeightSetZero(self):
        rec1 = Rectangle(7, 5)
        with self.assertRaises(ValueError):
            rec1.height = 0
    def test_HeightNormalCase(self):
        rec1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec1.height, 2)

    #x_testing----------------------------------------------------

    """tetsting if x is either float or not int"""
    def test_xisFloat(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle(1, 7, 3.5, 7, 12)

    """testing if c is str"""
    def test_Xistr(self):
        with self.assertRaises(TypeError):
            rec2 = Rectangle(1, 4, "x", 7, 1)

    """testing is x is less than 0"""
    def test_Xisless0(self):
        with self.assertRaises(ValueError):
            rec1 = Rectangle(1, 5, -3, 7, 12)
    if __name__ == "__main__":
        unittest.main()