#!/usr/bin/python3
"""Module for Rect, inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class rectangle, inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Constructor metod"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
