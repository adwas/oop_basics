#!/bin/env python3

class Car:
    ''' A car description '''
    NUMBER_OF_WHEELS = 4  # Class variable.

    def __init__(self, name):
        self.name = name
        self.distance = 0


mycar = Car("Fiat 126p")

print("My car %s has %d wheels." % (mycar.name, mycar.NUMBER_OF_WHEELS))
print("My car %s has %d wheels." % (mycar.name, Car.NUMBER_OF_WHEELS))
print(mycar.__dict__)


yourcar = Car("Porsche 911 GT")

print("Your car %s has %d wheels." % (yourcar.name, yourcar.NUMBER_OF_WHEELS))
print("Your car %s has %d wheels." % (yourcar.name, Car.NUMBER_OF_WHEELS))
print(yourcar.__dict__)
'''
My car Fiat 126p has 4 wheels.
My car Fiat 126p has 4 wheels.
{'name': 'Fiat 126p', 'distance': 0}
Your car Porsche 911 GT has 4 wheels.
Your car Porsche 911 GT has 4 wheels.
{'name': 'Porsche 911 GT', 'distance': 0}
'''
