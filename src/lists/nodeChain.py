#!/usr/bin/env python
"""
:created on: 05-09-2017
:modified on: 07-09-2017
:author: Miranda Aperghis
:contact: miranda.aperghis@gmail.com
"""


class Node(object):
    """A node has a value and a pointer to the next node in the chain"""

    def __init__(self, value):
        self.value = value
        self.next = None


def enumerateNodes(node):
    """Generator to enumerate all nodes
    :return: the next node in the chain
    :rtype: Node
    """
    while node != None:
        yield node
        node = node.next


if __name__ == '__main__':
    A = Node(1)
    B = Node(2)
    C = Node(3)
    A.nextNode(node=B)
    B.nextNode(node=C)
    printChain(node=A)
