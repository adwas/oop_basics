#!/bin/env python3

from enum import Enum
import random


class Gender(Enum):
    FEMALE = 'female'
    MALE = 'male'

    def isGender(value):
        return value in (Gender.MALE, Gender.FEMALE)

    def validate(value):
        if not Gender.isGender(value):
            raise ValueError('gender not valid')


class Human:

    def __init__(self, gender):
        Gender.validate(gender)
        self.gender = gender

    def __add__(self, other):
#        if(type(other) != Human):
        if not isinstance(other, Human):
            raise TypeError
        if self.gender == other.gender:
            return None
        return Human(list(Gender)[random.randrange(2)])

a = Human(Gender.MALE)
b = Human(Gender.FEMALE)

c = a + b

print(c.__dict__)
