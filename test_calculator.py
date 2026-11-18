import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(2, add(1, 1))
        self.assertEqual(5, add(4, 1))
        self.assertAlmostEqual(10.2, add(10, 0.2))

    def test_subtract(self): # 3 assertions
        self.assertEqual(0, sub(1, 1))
        self.assertEqual(-5, sub(0, 5))
        self.assertAlmostEqual(0.0, sub(5.6, 5.6))

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(2, logarithm(5, 25))
        self.assertEqual(3, logarithm(3, 27))
        self.assertEqual(4, logarithm(2, 16))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5, 5)
            logarithm(1, 5)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()