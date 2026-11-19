#https://github.com/dstructed/lab11-DM-TB
#Partner 1: Daniel Mendoza(dstructed
#Partner 2: Thomas Brandler

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(5, -4), 1)
        self.assertEqual(add(-5, 6), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, -5), 5)
        self.assertEqual(subtract(15, 0), 15)
        


    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(7, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(-4, 8), -2)
        self.assertAlmostEqual(divide(3, 1), 0.333333, places = 6)



    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    

    def test_logarithm(self): # 3 assertions
        self.assertEqual(5, 25), 2)
        self.assertEqual(3, 81), 4)
        self.assertAlmostEqual(10, 50), 1.69897, places = 5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 2)
    

    def test_log_invalid_argument(self): # 1 assertion
          with self.assertRaises(ValueError):
              logarithm(2, -1)


    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.4142136, places = 6)



    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(16),4)
        self.assertAlmostEqual(square_root(2), 1.4142136, places = 6)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
