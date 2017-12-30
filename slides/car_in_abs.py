#!/bin/env python3

from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):
    NUMBER_OF_WHEELS = 4

    @abstractmethod
    def drive(self, dist=0):
        pass

class VWCar (Car):

    def __init__(self, name="VW"):
        super().__init__() #is the same as super(VWCar, self).__init__()
        self.name = name
        self.distance = 0
        self.maxSpeed = 0

    def drive(self, dist=0):
        self.distance += dist

    def showName(self):
        print(self.name)

    def testEmission(self):
        raise NotImplementedError


class VWGolf (VWCar):

    def __init__(self, name="VW Golf"):
        super().__init__(name)
        self.maxSpeed = 210

    def testEmission(self):
        return True


class Skoda (VWGolf):

    def __init__(self, name="Skoda"):
        super().__init__(name)
        self.maxSpeed = 180

    def testEmission(self):
        if self.distance > 100_000:
            return False
        return True

if __name__ == '__main__':
    sk = Skoda()
    sk.drive(10)
    print(sk.__dir__)
    print(sk.__dict__)

    gl = VWGolf()
    gl.drive(30)
    print(gl.__dir__)
    print(gl.__dict__)

    # acar = Car()
    # acar = VWCar()
    # acar.testEmission()