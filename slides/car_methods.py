#!/bin/env python3

class Car:
    ''' A car description '''
    NUMBER_OF_WHEELS = 4  # Class variable.

    def __init__(self, name):
        self.name = name
        self.distance = 0

    def drive(self, distance):
        ''' incrises distance '''
        self.distance += distance

    def reverse(distance):
        ''' Class method '''
        print("distance %d" % distance)


mycar = Car("Fiat 126p")
print(mycar.__dict__)
mycar.drive(5)
print(mycar.__dict__)
Car.reverse(7)

