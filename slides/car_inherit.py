#!/bin/env python3


class Car:
    NUMBER_OF_WHEELS = 4

    def __init__(self, name):
        self.name = name
        self.distance = 0
        self.maxSpeed = 0

    def drive(self, dist=0):
        pass


class VWCar (Car):

    def __init__(self, name="VW"):
        super().__init__(name)
        self.maxSpeed = 200

    def drive(self, dist=0):
        self.distance += dist


class VWGolf (VWCar):

    def __init__(self, name="VW Golf"):
        super().__init__(name)
        self.maxSpeed = 210


class Skoda (VWGolf):

    def __init__(self, name="Skoda"):
        super().__init__(name)
        self.maxSpeed = 180


sk = Skoda()
sk.drive(10)
print(sk.__dir__)
print(sk.__dict__)

gl = VWGolf()
gl.drive(30)
print(gl.__dir__)
print(gl.__dict__)
