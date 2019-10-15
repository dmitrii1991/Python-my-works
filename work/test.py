import unittest
from main import *
from badcode import *


class TestTheFirstThreeTasks(unittest.TestCase):
    elements = [
        [1, 1, 1, 1, 1, 1],
        [23123, 334, 3424, 43, 32134],
        [0, 0, 0, 0, 0, 0],
        [234, 4, 3434, 31, 4],
        [324, '34234', '23434', 3434],
        ['34', '3432', '34234'],
        ['1', '1', '1'],
        ['0', '0'],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [0],
        ["1", "0"],
        [-1, -2, -3, -4],
        ['-1', -2, -5, -4],
    ]

    def test_math_squares_of_odd(self):
        self.assertEqual(math_squares_of_odd([1, 2, 4]), 1)
        self.assertEqual(math_squares_of_odd([1, 2, 5]), 26)
        self.assertEqual(math_squares_of_odd([3, 2, 6]), 9)
        self.assertEqual(math_squares_of_odd([1, 2, -1]), 2)

    def test_palindrome(self):
        self.assertEqual(palindrome("abba"), True)
        self.assertEqual(palindrome("bbaa"), True)
        self.assertEqual(palindrome("bcaaabc"), True)
        self.assertEqual(palindrome("bcbcbc"), False)
        self.assertEqual(palindrome("мадам"), True)
        self.assertEqual(palindrome("мадддамм"), False)

    def test_original_vs_optimized_code(self):
        for elem in self.elements:
            self.assertEqual(isFunnyFunction(elem), fun_func_without_correct(elem))

    def test_error(self):
        self.assertRaises(IndexError, lambda: isFunnyFunction([]))
        self.assertRaises(ValueError, lambda: isFunnyFunction(None))
        self.assertRaises(ValueError, lambda: fun_func_without_correct([]))
        self.assertRaises(ValueError, lambda: fun_func_with_correct([]))


if __name__ == '__main__':
    unittest.main()
