

class Node(object):
    '''A node has a value and a pointer to the next node in the chain'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def nextNode(self, node=None):
        '''Set next node'''
        if node:
            assert isinstance(node, Node), "next should be a Node instance"
            self.next = node
        return self.next


def printChain(node):
    '''Print a chain of nodes'''
    while node != None:
        print node.value
        node = node.nextNode()


if __name__ == '__main__':
    A = Node(1)
    B = Node(2)
    C = Node(3)
    A.nextNode(B)
    B.nextNode(C)
    printChain(A)
