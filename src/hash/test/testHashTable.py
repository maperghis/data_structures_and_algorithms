#!/usr/bin/env python
"""
:created on: 03-10-2017
:modified on: 03-10-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from src.hash.hashTable import HashTable
from src.hash.hashTableArrayNode import ArgumentException
from src.hash.nodePair import NodePair
import unittest


class TestHashTable(unittest.TestCase):
    """Tests for the HashTable class"""

    def setUp(self):
        self.table = HashTable()
        self.n1 = NodePair("susie", 25)
        self.n2 = NodePair("matt", 64)
        self.n3 = NodePair("alice", 29)
        self.n4 = NodePair("ross", 17)
        self.n5 = NodePair("jen", 85)
        self.n6 = NodePair("barney", 24)
        self.n7 = NodePair("charlie", 30)
        self.n8 = NodePair("zoe", 26)
        self.n9 = NodePair("ken", 72)

    def testGetIndex(self):
        """Test the getIndex method"""
        index = self.table.getIndex("hello world")
        self.assertEqual(index, 5)
        index = self.table.getIndex("hi there")
        self.assertEqual(index, 1)

    def testAdd(self):
        """Test the add method"""
        self.assertEqual(self.table.capacity(), 10)
        self.table.add(self.n1.key(), self.n1.value())
        self.assertTrue(self.table.contains(self.n1.key()))
        self.assertFalse(self.table.contains(self.n2.key()))
        self.table.add(self.n2.key(), self.n2.value())
        self.assertTrue(self.table.contains(self.n2.key()))
        self.table.add(self.n3.key(), self.n3.value())
        self.table.add(self.n4.key(), self.n4.value())
        self.table.add(self.n5.key(), self.n5.value())
        self.table.add(self.n6.key(), self.n6.value())
        self.table.add(self.n7.key(), self.n7.value())
        self.table.add(self.n8.key(), self.n8.value())
        self.assertEqual(self.table.capacity(), 10)
        self.table.add(self.n9.key(), self.n9.value())
        self.assertEqual(self.table.capacity(), 20)

    def testUpdate(self):
        """Test the update method"""
        self.table.add(self.n1.key(), self.n1.value())
        self.assertEqual(self.table.getValue(self.n1.key()), self.n1.value())
        self.table.update(self.n1.key(), 99)
        self.assertEqual(self.table.getValue(self.n1.key()), 99)
        self.assertRaises(ArgumentException, self.table.update, "jeremy", -42)

if __name__ == '__main__':
    unittest.main()
