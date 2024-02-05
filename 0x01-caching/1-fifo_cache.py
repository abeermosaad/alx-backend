#!/usr/bin/env python3
""" Basic dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache (BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Constructor of the class"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f'DISCARD: {list(self.cache_data.keys())[0]}')
                del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """ Get an item by key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
