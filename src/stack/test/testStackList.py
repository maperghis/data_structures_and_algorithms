#!/usr/bin/env python
"""
:created on: 08-09-2017
:modified on: 08-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import unittest
from src.stack.stackList import StackList, InvalidOperationException
from src.lists.doubleLinkedList import Node


class TestStackList(unittest.TestCase):
    """Test the StackList class"""

    def setUp(self):
        self.A = Node(1)
        self.B = Node(2)
        self.C = Node(3)
        self._stack = StackList()

    def test1(self):
        """Test the count, push, enumerate peek and pop methods"""
        self.assertEqual(self._stack.count(), 0)
        self._stack.push(self.A)
        self._stack.push(self.B)
        self._stack.push(self.C)
        for idx, node in enumerate(self._stack.enumerateStack()):
            if idx == 0:
                self.assertEqual(node.value, 3)
            elif idx == 1:
                self.assertEqual(node.value, 2)
            elif idx == 2:
                self.assertEqual(node.value, 1)
        self.assertEqual(self._stack.count(), 3)
        self.assertEqual(self._stack.peek(), 3)
        self.assertEqual(self._stack.count(), 3)
        self.assertEqual(self._stack.pop(), 3)
        self.assertEqual(self._stack.count(), 2)
        self.assertEqual(self._stack.pop(), 2)
        self.assertEqual(self._stack.count(), 1)
        self.assertEqual(self._stack.pop(), 1)
        self.assertEqual(self._stack.count(), 0)
        self.assertRaises(InvalidOperationException, self._stack.pop)

    def testClear(self):
        """Test the clear method"""
        self._stack.push(self.A)
        self._stack.push(self.B)
        self._stack.push(self.C)
        self._stack.clear()
        self.assertEqual(self._stack.count(), 0)
        self.assertRaises(InvalidOperationException, self._stack.pop)


if __name__ == '__main__':
    unittest.main()
