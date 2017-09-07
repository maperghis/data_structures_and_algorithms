#!/usr/bin/env python
"""
:created on: 07-09-2017
:modified on: 07-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import unittest
from src.lists.linkedList import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    """Test the LinkedList class"""

    def setUp(self):
        self.llist = LinkedList()
        self.A = Node(1)
        self.B = Node(2)
        self.C = Node(3)

    def testAddFirst(self):
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addFirst(self.A)
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.addFirst(self.B)
        self.assertEqual(self.llist.copyToList(), [2, 1])
        self.llist.addFirst(self.C)
        self.assertEqual(self.llist.copyToList(), [3, 2, 1])

    def testAddLast(self):
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addLast(self.A)
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.addLast(self.B)
        self.assertEqual(self.llist.copyToList(), [1, 2])
        self.llist.addLast(self.C)
        self.assertEqual(self.llist.copyToList(), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
