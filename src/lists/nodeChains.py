

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


def printChain(node):
    '''Print a chain of nodes'''
    while node != None:
        print node.value
        node = node.nextNode()


if __name__ == '__main__':
    A = Node(1)
    B = Node(2)
    C = Node(3)
    A.nextNode(node=B)
    B.nextNode(node=C)
    printChain(node=A)
