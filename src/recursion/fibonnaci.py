

class Fibonnaci(object):
    '''Implement a Fibonnaci Sequence in three different ways:
        - Recursively
        - Dynamically (Using Memoization to store results)
        - Iteratively'''

    def fib_rec(n):
        '''Recursively'''
        if n == 0 or n == 1:
            return n
        return fib_rec(n-1) + fib_rec(n-2)

    n = 10
    cache = [None] * (n + 1)

    def fib_dyn(n):
        '''Dynamically'''
        if n == 0 or n == 1:
            return n
        # Check cache
        if cache[n] != None:
            return cache[n]
        # Keep setting cache
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
        return cache[n]

    def fib_iter(n):
        '''Iteratively'''
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a
