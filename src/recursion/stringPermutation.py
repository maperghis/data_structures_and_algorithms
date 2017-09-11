#!/usr/bin/env python
"""
:created on: 04-09-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""


class StringPermutation(object):
    """Given a string, write a function that uses recursion to output a list of
    all the possible permutations of that string.
    For example, given s='abc' the function should return ['abc', 'acb', 'bac',
    'bca', 'cab', 'cba']
    """

    def permute(cls, s):
        """Find the permuations of a string"""
        if len(s) == 1:
            return s

        out = []
        for i, char in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [char + perm]
        return out
