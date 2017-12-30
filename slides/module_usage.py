#!/bin/env python3


import car_in_abs 
from car_in_abs import Skoda as Mycar

from foo import Bar


skoda = car_in_abs.Skoda()
skoda.showName()

mycar = Mycar()
mycar.showName()

bar = Bar()
bar.hello()
