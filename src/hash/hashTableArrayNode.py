#!/usr/bin/env python
"""
:created on: 28-09-2017
:modified on: 28-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from src.hash.nodePair import NodePair
from src.lists.doubleLinkedList import DoubleLinkedList


class ArgumentException(Exception):
    """Argument exception"""
    pass


class HashTableArrayNode(object):
    """A single linked list for a single slot in the hash table"""

    def __init__(self):
        self._items = DoubleLinkedList()

    def add(self, key, value):
        """Adds the key/value pair to the linked list.
        :param key: key to add
        :param value: value to add
        """
        for pair in self._items.enumerate():
            if pair.key() == key:
                raise ArgumentException("Hash table already contains the key")
        self._items.addFirst(NodePair(key, value))

    def update(self, key, value):
        """Updates the key/value pair in the linked list.
        :param key: key to update
        :param value: value to update
        """
        updated = False
        for pair in self._items.enumerate():
            if pair.key() == key:
                pair.value(value=value)
                updated = True
                break
        if not updated:
            raise ArgumentException("Hash table does not contains the key")

    def remove(self, key):
        """Removes an items from the linked list with the given key
        :param key: key to remove
        :returns: true if they key was removed
        """
        removed = False
        current = self._items.head
        while current != None:
            if current.value.key() == key:
                self._items.remove(current.value)
                removed = True
            current = current.next
        return removed

    def getValue(self, key):
        """Returns the value of a given key.
        :param key: the key we want the value of
        :returns: the value
        """
        for pair in self._items.enumerate():
            if pair.key() == key:
                return pair.value()
        raise ArgumentException("Hash table does not contains the key")

    def contains(self, key):
        """Find the key
        :param key: key to find
        :returns: true if the key exists
        """
        for pair in self._items.enumerate():
            if pair.key() == key:
                return True
        return False

    def clear(self):
        """Clear the linked list"""
        self._items.clear()

    def enumerate(self):
        """Enumerate all items in the linked list
        :returns: generator of NodePairs"""
        return self._items.enumerate()

    def enumerateKeys(self):
        """Enumerate keys
        :returns: generator of keys
        """
        for pair in self._items.enumerate():
            yield pair.key()

    def enumerateValues(self):
        """Enumerate values
        :returns: generator of values
        """
        for pair in self._items.enumerate():
            yield pair.value()

    def count(self):
        """Count the number of key value pairs
        :returns: number of items
        :rtype: integer
        """
        return self._items.count
