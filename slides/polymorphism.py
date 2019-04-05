#!/bin/env python3

class Figure:

    def area(self):
        print('Figure area')
        return 0

class Triangle:

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        print('Triangle area')
        return 0.5 * self.a * self.h

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print('Rectangle area')
        return self.a * self.b

class Square:

    def __init__(self, a):
        self.a = a


    def area(self):
        print('Square area')
        return self.a * self.a


figures = [ Square(5), Rectangle(2,3) , Triangle(4,3), Square(10) ]

figures_area = 0
for fig in figures:
    figures_area += fig.area()

print("figures_area = {}".format(figures_area))
