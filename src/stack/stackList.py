#!/usr/bin/env python
"""
:created on: 08-09-2017
:modified on: 08-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from src.lists.doubleLinkedList import DoubleLinkedList


class InvalidOperationException(Exception):
    """Invalid operation exception"""
    pass


class StackList(object):
    """Stack implemented using a doubly linked list"""

    def __init__(self):
        self._list = DoubleLinkedList()

    def push(self, item):
        """Push an item to the stack
        :param item: item being pushed to the stack
        """
        self._list.addFirst(item)

    def pop(self):
        """Pop an item from the stack
        :return: top item from the stack
        """
        if self._list.count == 0:
            raise InvalidOperationException("The stack is empty")
        value = self._list.head.value
        self._list.removeFirst()
        return value

    def peek(self):
        """Like pop, return an item from the stack but don't remove it
        :return: top item from the stack
        """
        if self._list.count == 0:
            raise InvalidOperationException("The stack is empty")
        value = self._list.head.value
        return value

    def count(self):
        """Count items
        :return: number of items in the stack
        :rtype: int
        """
        return self._list.count

    def clear(self):
        """Remove all items from the stack"""
        self._list.clear()

    def enumerateStack(self):
        """Enumerate all items in the stack"""
        return self._list.enumerate()
