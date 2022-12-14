from calc import SimpleCalc
import unittest
import pytest



class Calculator_tests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 5), 7)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(10, 2), 5)

    def test_percent(self):
        self.assertEqual(self.calc_obj.percent_calc(5,10), 50)

    def test_dob(self):
        self.assertEqual(self.calc_obj.dob(6, 1993), "6/1993")

    def test_cm_m(self):
        self.assertEqual(self.calc_obj.cm_to_m(1000), 10.0)












