#!/usr/bin/env python
"""
:created on: 03-10-2017
:modified on: 03-10-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from src.hash.hashTable import HashTable
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

    def testGetIndex(self):
        """Test the getIndex method"""
        index = self.table.getIndex("hello world")
        self.assertEqual(index, 5)
        index = self.table.getIndex("hi there")
        self.assertEqual(index, 1)

    def testAdd(self):
        """Test the add method"""
        self.table.add(self.n1.key(), self.n1.value())
        self.assertTrue(self.table.contains(self.n1.key()))
        self.assertFalse(self.table.contains(self.n2.key()))
        self.table.add(self.n2.key(), self.n2.value())
        self.assertTrue(self.table.contains(self.n2.key()))


if __name__ == '__main__':
    unittest.main()
