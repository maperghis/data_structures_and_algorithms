#!/usr/bin/env python
"""
:created on: 22-09-2017
:modified on: 22-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from src.lists.doubleLinkedList import Node
from src.queue.queueList import QueueList, InvalidOperationException
import unittest


class TestQueueList(unittest.TestCase):
    """Test the QueueList class"""

    def setUp(self):
        self.queue = QueueList()
        self.A = Node(1)
        self.B = Node(2)
        self.C = Node(3)

    def testEnqueue(self):
        self.queue.enqueue(self.A)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.enqueue(self.B)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.enqueue(self.C)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.count(), 3)
        for idx, item in enumerate(self.queue.enumerate()):
            if idx == 0:
                self.assertEqual(item.value, 1)
            elif idx == 1:
                self.assertEqual(item.value, 2)
            elif idx == 2:
                self.assertEqual(item.value, 3)

    def testDequeue(self):
        self.queue.enqueue(self.A)
        self.queue.enqueue(self.B)
        self.queue.enqueue(self.C)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.count(), 2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.count(), 1)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.count(), 0)
        self.assertRaises(InvalidOperationException, self.queue.dequeue)

if __name__ == '__main__':
    unittest.main()
