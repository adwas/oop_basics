# pylint: disable=C0111

import inspect
import unittest
from src import animals


class TestAnimalsCase(unittest.TestCase):

    def test_abstraction_of_Animal_class(self):
        self.assertTrue(inspect.isabstract(animals.Animal),
                        "Class animals.Animal should be abstract.")
        with self.assertRaises(TypeError):
            animal = animals.Animal()

    def test_Animal_class_has_say_hello_method(self):
        methods = inspect.getmembers(
            animals.Animal, predicate=inspect.isfunction)
        names = [methods[x][0] for x in range(len(methods))]
        self.assertIn("say_hello", names)

    def test_Animal_class_has_is_mammal_method(self):
        methods = inspect.getmembers(
            animals.Animal, predicate=inspect.isfunction)
        names = [methods[x][0] for x in range(len(methods))]
        self.assertIn("is_mammal", names)

    def test_Animal_class_has_is_carnivorous_method(self):
        methods = inspect.getmembers(
            animals.Animal, predicate=inspect.isfunction)
        names = [methods[x][0] for x in range(len(methods))]
        self.assertIn("is_carnivorous", names)

    def test_Cat_should_be_an_Animal(self):
        self.assertTrue(issubclass(animals.Cat, animals.Animal))

    def test_Cat_should_say_meow(self):
        a_cat = animals.Cat()
        self.assertEqual(a_cat.say_hello(), "Meow")

    def test_Cat_should_be_mammal(self):
        a_cat = animals.Cat()
        self.assertTrue(a_cat.is_mammal())

    def test_Cat_should_be_carnivorous(self):
        a_cat = animals.Cat()
        self.assertTrue(a_cat.is_carnivorous())

    def test_Dog_should_be_an_Animal(self):
        self.assertTrue(issubclass(animals.Dog, animals.Animal))

    def test_Dog_should_say_woof(self):
        a_dog = animals.Dog()
        self.assertEqual(a_dog.say_hello(), "Woof!...Woof!...Woof!")

    def test_Dog_should_be_mammal(self):
        a_dog = animals.Dog()
        self.assertTrue(a_dog.is_mammal())

    def test_Dog_should_be_carnivorous(self):
        a_dog = animals.Dog()
        self.assertTrue(a_dog.is_carnivorous())

    def test_Duck_should_be_an_Animal(self):
        self.assertTrue(issubclass(animals.Duck, animals.Animal))

    def test_Duck_should_say_quack(self):
        a_duck = animals.Duck()
        self.assertEquals(a_duck.say_hello(), "Quack...Quack")

    def test_Duck_should_not_be_mammal(self):
        a_duck = animals.Duck()
        self.assertFalse(a_duck.is_mammal())

    def test_Duck_should_not_be_carnivorous(self):
        a_duck = animals.Duck()
        self.assertFalse(a_duck.is_carnivorous())

    def test_Horse_should_be_an_Animal(self):
        self.assertTrue(issubclass(animals.Horse, animals.Animal))

    def test_Horse_should_say_neigh(self):
        a_horse = animals.Horse()
        self.assertEquals(a_horse.say_hello(), "Neigh")

    def test_Horse_should_be_mammal(self):
        a_horse = animals.Horse()
        self.assertTrue(a_horse.is_mammal())

    def test_Horse_should_not_be_carnivorous(self):
        a_horse = animals.Horse()
        self.assertFalse(a_horse.is_carnivorous())
