#!/usr/bin/env python3
"""
Task 3 - LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines a LRU caching system
    """
    def __init__(self):
        """
        Initializes with parent's constructor and sets up LRU order
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Caches a key-value pair. Evicts the newest if cache is full
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[0]))
                del self.cache_data[self.usage[0]]
                del self.usage[0]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value for a given key from the cache
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
