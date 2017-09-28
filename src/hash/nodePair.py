#!/usr/bin/env python
"""
:created on: 28-09-2017
:modified on: 28-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""


class NodePair(object):
    """A node in the hash table array"""

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def key(self):
        """The key cannot be changed because it would affect the indexing
        in the hash table.
        :returns: key
        """
        return self._key

    def value(self, value=None):
        """The value.
        :param value: new value
        :returns: value
        """
        if value:
            self._value = value
        return self._value
