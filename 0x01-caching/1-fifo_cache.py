#!/usr/bin/env python3
"""
Task 1 - FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initializes the FIFOCache object by calling the parent class
        constructor and setting up FIFO order
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair in the FIFO cache
        Args:
            key: The key for the item to be cached
            item: The value to be cached
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
        Retrieve the value associated with a given key from the FIFO cache
        Args:
            key: The key whose associated value is to be retrieved
        Returns:
            The value associated with the given key, or 
            None if the key is None or doesn't exist in the cache
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
