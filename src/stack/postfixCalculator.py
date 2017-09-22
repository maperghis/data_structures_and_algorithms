#!/usr/bin/env python
"""
:created on: 22-09-2017
:modified on: 22-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from src.stack.stackList import StackList
from src.lists.doubleLinkedList import Node


class ArgumentException(Exception):
    """Invalid argument exception"""
    pass


class Stack(StackList):
    '''Extention of a stack class implemented using a linked list which can
    take any item and create a Node instance internally'''

    def push(self, item):
        """Push an item to the stack
        :param item: item being pushed to the stack
        """
        if not isinstance(item, Node):
            item = Node(item)
        self._list.addFirst(item)


class PostfixCalculator(object):
    '''Implementation of a postfix calculator using a Stack'''

    def add(self, lhs, rhs):
        """Addition"""
        return lhs + rhs

    def subtract(self, lhs, rhs):
        """Subtraction"""
        return lhs - rhs

    def multiply(self, lhs, rhs):
        """Multiplication"""
        return lhs * rhs

    def divide(self, lhs, rhs):
        """Division"""
        return lhs / rhs

    def modulo(self, lhs, rhs):
        """Modulus"""
        return lhs % rhs

    def run(self, *args):
        """Run the calculator with some arguments"""
        stack = Stack()
        for item in args:
            if isinstance(item, int):
                stack.push(item)
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                switcher = {
                    '+': self.add,
                    '-': self.subtract,
                    '*': self.multiply,
                    '/': self.divide,
                    '%': self.modulo
                }
                func = switcher.get(item)
                if not func:
                    raise ArgumentException("Unrecognised token: {0}", item)
                stack.push(func(lhs, rhs))
        return stack.pop()
