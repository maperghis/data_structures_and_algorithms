#!/usr/bin/env python
"""
:created on: 22-09-2017
:modified on: 22-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from src.lists.doubleLinkedList import DoubleLinkedList


class InvalidOperationException(Exception):
    """Invalid operation exception"""
    pass


class QueueList(object):
    """Queue implemented using a doubly linked list"""

    def __init__(self):
        self._list = DoubleLinkedList()

    def enqueue(self, item):
        """Add an item to the back of the queue"""
        self._list.addLast(item)

    def dequeue(self):
        """Remove and return front item from the queue"""
        if self._list.count == 0:
            raise InvalidOperationException("The queue is empty.")
        val = self._list.head.value
        self._list.removeFirst()
        return val

    def peek(self):
        """Returns the front item in the queue without removing it"""
        if self._list.count == 0:
            raise InvalidOperationException("The queue is empty.")
        return self._list.head.value

    def count(self):
        """Number of items in the queue"""
        return self._list.count

    def clear(self):
        """Clear the items in the list"""
        self._list.clear()

    def enumerate(self):
        """Enumerate all the items in the list"""
        return self._list.enumerate()
