#!/usr/bin/env python
"""
:created on: 04-09-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import collections


class MissingElement(object):
    """Consider an array of non-negative integers. A second array is formed by
    shuffling the elements of the first array and deleting a random element.
    Given these two arrays, find which element is missing in the second
    array."""

    def finder1(cls, arr1, arr2):
        """My solution 0(n)"""
        arr1.sort()
        new_arr = sorted(arr2)
        for num in arr1:
            if num not in new_arr:
                return num
            else:
                index = new_arr.index(num)
                new_arr = new_arr[:index] + new_arr[index+1:]
        return -1

    def finder2(cls, arr1, arr2):
        """Alternative solution O(nlogn)"""
        arr1.sort()
        arr2.sort()

        for num1, num2 in zip(arr1, arr2):
            if num1 != num2:
                return num1
        return arr1[-1]

    def finder3(cls, arr1, arr2):
        """Alternative solution O(n)"""
        d = collections.defaultdict(int)
        for num in arr2:
            d[num] += 1
        for num in arr1:
            if d[num] == 0:
                return num
            else:
                d[num] -= 1
