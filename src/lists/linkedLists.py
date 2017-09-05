'''Linked lists are a single chain of nodes, providing a head & tail pointer
and operations to add, remove, find and enumerate. Linked lists have very
efficient insertion
'''

class Node(object):
    '''A node has a value and a pointer to the next node in the chain'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def nextNode(self, **kwargs):
        '''Set next node'''
        # Slight change to my usual implementation, can't use my usual node=None
        #   because sometimes we want to change the next node to None!
        #   Use kwargs instead.
        if 'node' in kwargs:
            self.next = kwargs.get('node')
        return self.next


class LinkedList(object):
    '''Implementation of a linked list'''

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addFirst(self, node):
        '''Add a node to the start of the linked list, this operation has a
        constant time complexity regardless of the number of nodes in the
        linked list.'''
        temp = self.head
        self.head = node
        node.nextNode(node=temp)
        self.count += 1
        if self.count == 1:
            self.tail = self.head

    def addLast(self, node):
        '''Add a node to the end of the linked list, this operation has a
        constant time complexity regardless of the number of nodes in the
        linked list.'''
        if self.count == 0:
            self.head = node
        else:
            self.tail.nextNode(node=node)
        self.tail = node
        self.count += 1

    def removeFirst(self):
        '''Remove the first node from the list, this operation has a constant
        time complexity.'''
        if self.count != 0:
            self.head = self.head.nextNode()
            self.count -= 1
            if self.count == 1:
                self.tail = None

    def removeLast(self):
        '''Remove the last node from the list, this operation requires
        enumerating over all elements in the list. This is because we only
        store the head and tail references and we need to update the second to
        last node.
        This operation has time complexity O(n).'''
        if self.count != 0:
            if self.count == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.nextNode() != self.tail:
                    current = current.nextNode()
                current.nextNode(node=None)
                self.tail = current
            self.count -= 1

    def enumerate(self):
        '''Enumerate over the linked list'''
        if self.head:
            node = self.head
            while node != None:
                yield node
                node = node.nextNode()

    def __str__(self):
        '''String representation'''
        ret = []
        if self.head != None:
            node = self.head
            while node != None:
                ret.append(node.value)
                node = node.nextNode()
        return str(ret)


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
