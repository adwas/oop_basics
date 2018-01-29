'''
Create class Temerature that holds a temperature in Fahrenheit
and provide methods to convert to Celsius and Kelvin.
Insert it in monitor package.

T(°C) = (T(°F) - 32) × 5/9
T(K) = (T(°F) + 459.67)× 5/9
T(K) = T(°C) + 273.15

Conversion results should be rounded to two digits.

PL:
Napisz klasę Temerature ktora przechowuje wartość temperatury w Fahrenheitach
i ma metody do konwersji wartości do Celcjusza i Kelwina.

Każda konwersja powinna powinna zaokrąglać wynik do dwóch miejsc po przecinku.

'''
import unittest
from src import monitor

class TestTemperatureCase(unittest.TestCase):

    def test_fahrenheit_temperature_monitor(self):

        temp = monitor.Temperature(-40)

        self.assertEqual(temp.as_fahrenheit(), -40.0,
                         ' Incorrect fahrenheit value')
        self.assertEqual(temp.as_celsius(), -40.0,
                         ' Incorrect celsius value')
        self.assertEqual(temp.as_kelvin(), 233.15,
                         ' Incorrect kelvin value')


    def test_float_fahrenheit_temperature_monitor(self):

        temp = monitor.Temperature(-459.673456)

        self.assertEqual(temp.as_fahrenheit(), -459.67,
                         ' Incorrect fahrenheit value')
        self.assertEqual(temp.as_celsius(), -273.15,
                         ' Incorrect celsius value')
        self.assertEqual(temp.as_kelvin(), 0,
                         ' Incorrect kelvin value')

