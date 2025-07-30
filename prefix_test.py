import unittest

class PrefixTestCase(unittest.
TestCase):
   def test_prefix():
    prefixs = ["flower", "flow", "flight"]
    expected = "fl"
    actual = prefix(prefixs)
    self.asserEqual(actual, expected)
