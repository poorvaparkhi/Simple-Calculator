import unittest
from my_code import *

class CalculatorTest(unittest.TestCase):

    def test_onempty_should_return_zero(self):
        self.assertEqual(add(''), 0)

    def test_sum_of_one_number(self):
        self.assertEqual(add('1'), 1)

    def test_sumof_two_numbers(self):
        self.assertEqual(add('1,2'), 3)

    def test_multiple_numbers_sum(self):
        self.assertEquals(add('1,2,3,4,5'), 15)

    def test_sum_of_numbers_delimited_by_newline(self):
        self.assertEquals(add('1\n2\n,3\n\n,'), 6)

    def test_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            add('-1,-2')
        self.assertTrue('negatives not allowed' in context.exception)

    def test_greater_then_thousand(self):
        self.assertEquals(add('2000,2,99,88,4000'), 189)

    def test_multiple_delimiters(self):
        self.assertEquals(add('//[*][%]\n1*2%3'), 6)