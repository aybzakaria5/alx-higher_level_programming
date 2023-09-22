#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    r3 = Square(2, 3, 4, 1)
    Rectangle.save_to_file([r1, r2, r3])

    with open("Rectangle.json", "r") as file:
        print(file.read())