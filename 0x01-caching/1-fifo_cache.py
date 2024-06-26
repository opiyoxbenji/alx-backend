#!/usr/bin/env python3
"""
Task 1 - FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a FIFO caching system
    """

    def __init__(self):
        """
        Initializes with parent's constructor and sets up FIFO order
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Caches a key-value pair. Evicts oldest if cache is full
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value for a given key from the cache
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
