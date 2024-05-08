#!/usr/bin/env python3
"""
Task 0 - Caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    
    Methods:
        put(key, item) - store a key-value pair in the cache
        get(key) - retrieve the value associated with a given key from the cache
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Store a key-value pair in the cache

        Args:
            Key: The key for the item to be stored
            Item: The value to be stored
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with a given key from cache
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
