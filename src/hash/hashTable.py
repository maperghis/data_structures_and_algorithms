#!/usr/bin/env python
"""
:created on: 28-09-2017
:modified on: 28-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com

A hash table is a key/value associative collection.
"""
from src.hash.HashTableArrayNode import HashTableArrayNode


class HashTable(object):
    """Impementation of a hash table using linked list chaining to
    handle collisions."""

    def __init__(self, capacity=None):
        initialCapacity = capacity if capacity is not None else 10
        assert isinstance(initialCapacity, int)
        assert initialCapacity >= 1
        self._hashTable = [HashTableArrayNode()] * initialCapacity
        # If the array exceeds this fill percentage it will grow
        self._fillFactor = 0.75
        self._maxItemsAtCurrentSize = int(initialCapacity * self._fillFactor) + 1
        self._count = 0

    def add(self, key, value):
        """Adds the key/value pair to the node.
        :param key: new key to add
        :param value: new value to add
        """
        if self._count >= self._maxItemsAtCurrentSize:
            largerHashTable = [HashTableArrayNode()] * (self.capacity() * 2)
            for node in self.enumerate():
                largerHashTable[getIndex(node.key)].add(node.key, node.value)
            self._hashTable = largerHashTable
            self._maxItemsAtCurrentSize = int(self.capacity() * self._fillFactor) + 1
        self._hashTable[getIndex(key)].add(key, value)
        self._count += 1

    def update(self, key, value):
        """Update the value of the existing key/value pair.
        :param key: key to update
        :param value: new value
        """
        self._hashTable[getIndex(key)].update(key, value)

    def remove(self, key):
        """Remove the key
        :param key: key to remove
        :returns: true if the key was removed
        """
        removed = self._hashTable[getIndex(key)].remove(key):
        if removed:
            self._count -= 1
        return removed

    def getValue(self, key):
        """Finds and returns the value for the specified key
        :param key: key to find
        :returns: value of the given key
        """
        return self._hashTable[getIndex(key)].getValue(key)

    def contains(self, key):
        """Returns true if the key exists in the hash table
        :param key: key to find
        :returns: true if the key was found
        """
        return self._hashTable[getIndex(key)].contains(key)

    def capacity(self):
        """The capacity of the hash table array
        :returns: capacity of the hash table array
        :rtype: int
        """
        return len(self._hashTable)

    def clear(self):
        """Removes every item from the hash table array"""
        for node in self._hashTable:
            node.clear()
        self._count = 0
        self._maxItemsAtCurrentSize = int(initialCapacity * self._fillFactor) + 1

    def enumerate(self):
        """Enumerate all the values in the hash table
        :returns: generator to enumerate all NodePairs
        """
        for node in self._hashTable:
            yield node.enumerate()

    def count(self):
        """The number of items in the hash table
        :returns: count of items in the hash table
        :rtype: int
        """
        return self._count
