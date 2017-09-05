'''Linked lists are a single chain of nodes, providing a head & tail pointer
and operations to add, remove, find and enumerate. Linked lists have very
efficient insertion
'''

class Node(object):
    '''A node has a value and a pointer to the next node in the chain'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def nextNode(self, node=None):
        '''Set next node'''
        if node:
            self.next = node
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
        node.nextNode(temp)
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
            self.tail.nextNode(node)
        self.tail = node
        self.count += 1

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
                current.nextNode(None)
                self.tail = current
            self.count -= 1

    def __str__(self):
        '''String representation'''
        head = None if not self.head else self.head.value
        tail = None if not self.tail else self.tail.value
        return "Head:{0} Tail:{1} Count:{2}".format(head, tail, self.count)


if __name__ == '__main__':
    llist = LinkedList()
    print str(llist)
    A = Node(3)
    llist.addFirst(A)
    print str(llist)
    B = Node(8)
    llist.addFirst(B)
    print llist
    C = Node(1)
    llist.addLast(C)
    print llist
    D = Node(2)
    llist.addLast(D)
    print llist
    llist.removeLast()
    print llist
