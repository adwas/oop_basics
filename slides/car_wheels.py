#!/bin/env python3

class Car:                                                  # class definition
    ''' A car description '''
    number_of_wheels = 4                                    # Class variable. Accessible by Car.number_of_wheels.

mycar = Car()                                               # mycar is an object instance of Car class
print('My car has %d wheels' % mycar.number_of_wheels)      # mycar.number_of_wheels refers to Car.number_of_wheels

print("Generally car has %d wheels" % Car.number_of_wheels) # Generally car has 4 wheels

yourcar = Car()                                             # mycar is an object instance of Car class
yourcar.number_of_wheels = 3                                # Note: we are modifing instance reference. From now yourcar has own copy
print('Your car has %d wheels' % yourcar.number_of_wheels)  # Your car has 3 wheels
print('My car has %d wheels' % mycar.number_of_wheels)      # My car has 4 wheels
print("Generally car has %d wheels" % Car.number_of_wheels) # Generally car has 4 wheels

Car.number_of_wheels = 5                                    # Modification on class level
strangecar = Car()
print('Strange car has %d wheels' % strangecar.number_of_wheels) # Strange car has 5 wheels
print('Your car has %d wheels' % yourcar.number_of_wheels)  # Your car has 3 wheels
print('My car has %d wheels' % mycar.number_of_wheels)      # My car has 5 wheels. Upppssss
