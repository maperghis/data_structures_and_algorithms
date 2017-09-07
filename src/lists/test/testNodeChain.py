#!/usr/bin/env python
"""
:created on: 07-09-2017
:modified on: 07-09-2017
:author: Miranda Aperghis
:contact: miranda.aperghis@gmail.com
"""
import unittest
from src.lists.nodeChain import Node, enumerateNodes


class TestNodeChain(unittest.TestCase):
    """Test the NodeChain class"""

    def testNodeChain(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next = node2
        node2.next = node3
        res = []
        for n in enumerateNodes(node1):
            res.append(n.value)
        self.assertItemsEqual(res, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
