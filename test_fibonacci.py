import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_of_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_of_one(self):
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_of_two(self):
        self.assertEqual(fibonacci(2), 1)
        
    def test_fibonacci_of_three(self):
        self.assertEqual(fibonacci(3), 2)
        
    def test_fibonacci_of_four(self):
        self.assertEqual(fibonacci(4), 3)
        
    def test_fibonacci_of_five(self):
        self.assertEqual(fibonacci(5), 5)


