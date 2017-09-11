#!/usr/bin/env python
"""
:created on: 04-09-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""


class LargestContinuousSum(object):
    """Given an array of integers (positive and negative) find the largest
    continuous sum."""

    def large_cont_sum(cls, arr):
        """Solution"""
        if len(arr) == 0:
            return 0
        max_sum = current_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum
