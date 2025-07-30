import unittest
from palindrome import palindrome

class PalindromeTestCase(unittest.TestCase):
   def test_palindrome(self):
        number = 1551
        expected = True
        actual = palindrome(number)
        self.assertEqual(expected, actual)
