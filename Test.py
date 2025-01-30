#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_init(self):
        #test case to add two numbers
        data = [23,32]
        result = summation(data)
        self.assertEqual(result,5)
if __name__=='__main__':
    unittest.main()
