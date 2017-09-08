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
        self.D = Node(3)

    def testAddFirst(self):
        """Test the LinkedList.addFirst method"""
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addFirst(self.A)
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.addFirst(self.B)
        self.assertEqual(self.llist.copyToList(), [2, 1])
        self.llist.addFirst(self.C)
        self.assertEqual(self.llist.copyToList(), [3, 2, 1])

    def testAddLast(self):
        """Test the LinkedList.addLast method"""
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addLast(self.A)
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.addLast(self.B)
        self.assertEqual(self.llist.copyToList(), [1, 2])
        self.llist.addLast(self.C)
        self.assertEqual(self.llist.copyToList(), [1, 2, 3])

    def testRemoveFirst(self):
        """Test the LinkedList.removeFirst method"""
        self.llist.removeFirst()
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addFirst(self.A)
        self.llist.removeFirst()
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addFirst(self.A)
        self.llist.addFirst(self.B)
        self.llist.removeFirst()
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.addFirst(self.B)
        self.llist.addFirst(self.C)
        self.llist.removeFirst()
        self.assertEqual(self.llist.copyToList(), [2, 1])
        self.llist.removeFirst()
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.removeFirst()
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.removeFirst()
        self.assertEqual(self.llist.copyToList(), [])

    def testRemoveLast(self):
        """Test the LinkedList.removeLast method"""
        self.llist.removeLast()
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addLast(self.A)
        self.llist.removeLast()
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addLast(self.A)
        self.llist.addLast(self.B)
        self.llist.removeLast()
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.addLast(self.B)
        self.llist.addLast(self.C)
        self.llist.removeLast()
        self.assertEqual(self.llist.copyToList(), [1, 2])
        self.llist.removeLast()
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.removeLast()
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.removeLast()
        self.assertEqual(self.llist.copyToList(), [])

    def testRemove(self):
        """Test the LinkedList.remove method"""
        self.llist.remove(3)
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addFirst(self.A)
        self.llist.remove(3)
        self.assertEqual(self.llist.copyToList(), [1])
        self.llist.remove(1)
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addFirst(self.C)
        self.llist.addFirst(self.D)
        self.assertEqual(self.llist.copyToList(), [3, 3])
        self.llist.remove(3)
        self.assertEqual(self.llist.copyToList(), [])
        self.llist.addFirst(self.A)
        self.llist.addLast(self.C)
        self.llist.addLast(self.D)
        self.assertEqual(self.llist.copyToList(), [1, 3, 3])
        self.llist.remove(3)
        self.assertEqual(self.llist.copyToList(), [1])

    def testEnumerate(self):
        """Test the LinkedList.enumerate method"""
        self.llist.addLast(self.A)
        self.llist.addLast(self.B)
        self.llist.addLast(self.C)
        self.llist.addLast(self.D)
        for idx, node in enumerate(self.llist.enumerate()):
            if idx == 0:
                self.assertEqual(node.value, 1)
            elif idx == 1:
                self.assertEqual(node.value, 2)
            elif idx == 2:
                self.assertEqual(node.value, 3)
            elif idx == 3:
                self.assertEqual(node.value, 3)

    def testContains(self):
        """Test the LinkedList.contains method"""
        self.llist.addLast(self.A)
        self.llist.addLast(self.B)
        self.llist.addLast(self.C)
        self.llist.addLast(self.D)
        self.assertTrue(self.llist.contains(1))
        self.assertTrue(self.llist.contains(2))
        self.assertTrue(self.llist.contains(3))
        self.assertFalse(self.llist.contains(4))


if __name__ == '__main__':
    unittest.main()
