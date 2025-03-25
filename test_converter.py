import unittest
from fahrenheit_to_celsius import fahrenheit_to_celsius

class TestTemperatureConversion(unittest.TestCase):
    def test_conversion(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(100), 37.78, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.00, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.00, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.00, places=2)

if __name__ == '__main__':
    unittest.main()
