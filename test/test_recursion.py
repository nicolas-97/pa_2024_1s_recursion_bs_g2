import unittest
from algorithms.recursion import factorial, fibonacci, sum_of_numbers, power, max_in_list

class TestRecursion(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_sum_of_numbers(self):
        self.assertEqual(sum_of_numbers(0), 0)
        self.assertEqual(sum_of_numbers(1), 1)
        self.assertEqual(sum_of_numbers(5), 15)

    def test_power(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 4), 81)

    def test_max_in_list(self):
        self.assertEqual(max_in_list([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_in_list([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_in_list([5, 2, 9, 1, 7]), 9)

if __name__ == '__main__':
    unittest.main()
