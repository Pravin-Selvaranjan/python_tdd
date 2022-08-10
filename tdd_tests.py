from calc import SimpleCalc
import pytest
import unittest



class Calculator_tests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2,5), 7)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(10,5), 5)




