import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_of_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_of_one(self):
        self.assertEqual(fibonacci(1), 1)


