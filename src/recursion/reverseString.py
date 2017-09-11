#!/usr/bin/env python
"""
:created on: 04-09-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""


class ReverseString(object):
    """Reverse a string using recursion"""

    def reverse(s):
        """My solution, base case when length of string is less than or equal
        to 1"""
        if len(s) <= 1:
            return s
        last_ele = len(s) - 1
        return s[last_ele] + reverse(s[:last_ele])

    def reverse(s):
        """Other solution is a bit cleaner"""
        if len(s) <= 1:
            return s

        return reverse(s[1:]) + s[0]
