#!/usr/bin/env python
"""
:created on: 05-09-2017
:modified on: 08-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com

Double Linked Lists is a single chain of nodes which provide pointers to the
head and tail of the chain. Each node has a pointer to the next and the
previous node. This class provides operations to add, remove, find and
enumerate nodes.
"""


class Node(object):
    """A node has a value, a pointer to the next node in the chain and a
    pointer to the previous node in the chain"""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList(object):
    """Implementation of a double linked list"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addFirst(self, node):
        """Add a node to the start of the linked list. This operation has a
        constant time complexity regardless of the number of nodes in the
        linked list.
        :param node: node to insert
        :type node: Node
        """
        # Before: Head ------> 2 <-> 3 -> None
        # After: Head -> 1 <-> 2 <-> 3 -> None
        temp = self.head
        self.head = node
        node.next = temp
        if self.count == 0:
            # list was empty so set tail
            self.tail = self.head
        else:
            temp.previous = self.head
        self.count += 1

    def addLast(self, node):
        """Add a node to the end of the linked list. This operation has a
        constant time complexity regardless of the number of nodes in the
        linked list.
        :param node: node to insert
        :type node: Node
        """
        # Before: Head -> 1 <-> 2 -> None
        # After:  Head -> 1 <-> 2 <-> 3 -> None
        if self.count == 0:
            self.head = node
        else:
            self.tail.next=node
            node.previous = self.tail
        self.tail = node
        self.count += 1

    def removeFirst(self):
        """Remove the first node from the linked list. This operation has a
        constant time complexity."""
        if self.count != 0:
            # Before: Head -> 1 <-> 2 -> None
            # After:  Head -------> 2 -> None
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.count -= 1
            if self.count == 0:
                self.tail = None
            else:
                self.head.previous = None

    def removeLast(self):
        """Remove the last node from the linked list. This operation is better
        than in a linked list because we don't have to enumerate over all the
        nodes to find the second to last node, we can just use the previous
        pointer. This is much better than the linked list, it changes it from
        O(n) to O(1)"""
        if self.count != 0:
            if self.count == 1:
                temp = self.head
                self.head = None
                self.tail = None
                temp.next = None
            else:
                # Before: Head -> 1 <-> 2 <-> 3 -> None
                # After:  Head -> 1 <-> 2 -------> None
                temp = self.tail
                self.tail.previous.next = None
                self.tail = self.tail.previous
                temp.previous = None
            self.count -= 1

    def remove(self, value):
        """Remove an item from the linked list given its value. This operation
        has at best, a constant time complexity and at worst, O(n).
        1) empty list - do nothing
        2) single node (previous is None)
        3) many nodes:
            a) node to remove is the first node
            b) node to remove is in the middle or end
        :param value: remove node with this property
        """
        previous = None
        current = self.head
        while current != None:
            if current.value == value:
                if previous != None:
                    # Case 3b, node is in middle or end
                    previous.next=current.next
                    if current.next == None:
                        # It was the end so update tail
                        # Before: Head -> 3 <-> 5 -> None
                        # After:  Head -> 3 ------> None
                        self.tail = previous
                    else:
                        current.next.previous = previous
                    self.count -= 1
                    # Middle node removed needs next pointer set to None
                    # Before: Head -> 3 <-> 5 -> 7 -> None
                    # After:  Head -> 3 <------> 7 -> None
                    #   previous = 3, current = 5
                    #   current.next = 7
                    #   so 7.previous = 3
                    temp = current
                    current = current.next
                    temp.next = None
                    temp.previous = None
                else:
                    # 3a, node is first
                    self.head = self.head.next
                    # Before: Head -> 3 <-> 5 -> None
                    # After: Head -------> 5 -> None
                    #   previous = head, current = 3
                    #   current.next = 5
                    #   so 5.previous = None
                    temp = current
                    current = current.next
                    temp.next = None
                    temp.previous = None
                    self.count -= 1
                    if self.count == 0:
                        previous = None
                        self.tail = None
                    else:
                        current.previous = None
            else:
                previous = current
                current = current.next

    def enumerate(self):
        """Enumerate over the linked list"""
        if self.head:
            node = self.head
            while node != None:
                yield node
                node = node.next

    def contains(self, value):
        """Check to see if the linked list contains the given value"""
        for node in self.enumerate():
            if node.value == value:
                return True
        return False

    def copyToList(self):
        """Copy linked list to a python list object
        :returns: linked list as a list
        :rtype: List
        """
        ret = []
        for node in self.enumerate():
            ret.append(node.value)
        return ret

    def clear(self):
        """Clear linked list"""
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        """String representation"""
        return str(self.copyToList())


if __name__ == '__main__':
    llist = LinkedList()
    print "start", llist
    A = Node(3)
    llist.addFirst(A)
    print "add first 3", llist
    B = Node(8)
    llist.addFirst(B)
    print "add first 8", llist
    C = Node(1)
    llist.addLast(C)
    print "add last 1", llist
    D = Node(2)
    llist.addLast(D)
    print "add last 2", llist
    llist.removeLast()
    print "remove last", llist
    llist.removeFirst()
    print "remove first", llist
    nodes = llist.enumerate()
    for n in nodes:
        print n.value
    print llist.contains(1)
    print llist.contains(9)
    print llist.copyToList()
    llist.remove(1)
    print "remove 1", llist
    llist.clear()
    print "clear", llist
