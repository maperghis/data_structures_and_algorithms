#!/usr/bin/env python
"""
:created on: 29-09-2017
:modified on: 29-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import unittest
from src.hash.nodePair import NodePair
from src.hash.hashTableArrayNode import HashTableArrayNode, ArgumentException


class TestHashTableArrayNode(unittest.TestCase):
    """Tests for the TestHashTableArrayNode class"""

    def setUp(self):
        self.arr = HashTableArrayNode()
        self.n1 = NodePair("susie", 25)
        self.n2 = NodePair("matt", 64)
        self.n3 = NodePair("alice", 29)
        self.n4 = NodePair("ross", 17)

    def testAdd(self):
        """Test the add method"""
        self.arr.add(self.n1.key(), self.n1.value())
        self.arr.add(self.n2.key(), self.n2.value())
        self.arr.add(self.n3.key(), self.n3.value())
        self.arr.add(self.n4.key(), self.n4.value())
        for idx, pair in enumerate(self.arr.enumerate()):
            if idx == 0:
                self.assertEqual(pair, self.n4)
            elif idx == 1:
                self.assertEqual(pair, self.n3)
            elif idx == 2:
                self.assertEqual(pair, self.n2)
            elif idx == 3:
                self.assertEqual(pair, self.n1)
            else:
                self.fail("Too many node pairs in the array")

    def testUpdate(self):
        """Test for the update method"""
        self.arr.add(self.n1.key(), self.n1.value())
        for pair in self.arr.enumerate():
            self.assertEqual(pair, self.n1)
        self.arr.update(self.n1.key(), 99)
        for pair in self.arr.enumerate():
            self.assertEqual(pair.key(), self.n1.key())
            self.assertEqual(pair.value(), 99)
        self.arr.update(self.n1.key(), -42)
        for pair in self.arr.enumerate():
            self.assertEqual(pair.key(), self.n1.key())
            self.assertEqual(pair.value(), -42)
        self.assertRaises(ArgumentException, self.arr.update, "jeremey", 50)

    def testRemove(self):
        """Test for the remove method"""
        self.arr.add(self.n1.key(), self.n1.value())
        for pair in self.arr.enumerate():
            self.assertEqual(pair, self.n1)
        self.assertEqual(self.arr.count(), 1)
        success = self.arr.remove(self.n1.key())
        self.assertTrue(success)
        self.assertEqual(self.arr.count(), 0)
        success = self.arr.remove(self.n1.key())
        self.assertFalse(success)

    def testGetValue(self):
        """Test for the getValue method"""
        self.arr.add(self.n1.key(), self.n1.value())
        self.assertEqual(self.arr.getValue(self.n1.key()), self.n1.value())
        self.assertRaises(ArgumentException, self.arr.getValue, "jeremy")

    def testContains(self):
        """Test for the contains method"""
        self.arr.add(self.n1.key(), self.n1.value())
        self.assertTrue(self.arr.contains(self.n1.key()))
        self.assertFalse(self.arr.contains("jeremy"))

    def testClear(self):
        """Test for the clear method"""
        self.arr.add(self.n1.key(), self.n1.value())
        self.assertEqual(self.arr.count(), 1)
        self.arr.clear()
        self.assertEqual(self.arr.count(), 0)

    def testEnumerateKeys(self):
        """Test for the enumerateKeys method"""
        self.arr.add(self.n1.key(), self.n1.value())
        self.arr.add(self.n2.key(), self.n2.value())
        self.arr.add(self.n3.key(), self.n3.value())
        self.arr.add(self.n4.key(), self.n4.value())
        for idx, key in enumerate(self.arr.enumerateKeys()):
            if idx == 0:
                self.assertEqual(key, self.n4.key())
            elif idx == 1:
                self.assertEqual(key, self.n3.key())
            elif idx == 2:
                self.assertEqual(key, self.n2.key())
            elif idx == 3:
                self.assertEqual(key, self.n1.key())
            else:
                self.fail("Too many node pairs in the array")

    def testEnumerateValues(self):
        """Test for the enumerateValues method"""
        self.arr.add(self.n1.key(), self.n1.value())
        self.arr.add(self.n2.key(), self.n2.value())
        self.arr.add(self.n3.key(), self.n3.value())
        self.arr.add(self.n4.key(), self.n4.value())
        for idx, value in enumerate(self.arr.enumerateValues()):
            if idx == 0:
                self.assertEqual(value, self.n4.value())
            elif idx == 1:
                self.assertEqual(value, self.n3.value())
            elif idx == 2:
                self.assertEqual(value, self.n2.value())
            elif idx == 3:
                self.assertEqual(value, self.n1.value())
            else:
                self.fail("Too many node pairs in the array")


if __name__ == '__main__':
    unittest.main()
