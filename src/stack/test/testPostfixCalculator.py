#!/usr/bin/env python
"""
:created on: 22-09-2017
:modified on: 22-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import unittest
from src.stack.postfixCalculator import PostfixCalculator, ArgumentException


class TestPostfixCalculator(unittest.TestCase):
    """Test cases for the PostfixCalculator class"""

    def setUp(self):
        self.cal = PostfixCalculator()

    def testCalculator(self):
        self.assertEqual(self.cal.run(8, 2, '+'), 10)
        self.assertEqual(self.cal.run(8, 2, '-'), 6)
        self.assertEqual(self.cal.run(8, 2, '*'), 16)
        self.assertEqual(self.cal.run(8, 2, '/'), 4)
        self.assertEqual(self.cal.run(8, 2, '%'), 0)
        self.assertRaises(ArgumentException, self.cal.run, 8, 2, ')')
        self.assertEqual(self.cal.run(5, 6, 7, '*', '+', 1, '-'), 46)


if __name__ == '__main__':
    unittest.main()
