#!/usr/bin/env python3
""" Basic dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache (BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Constructor of the class"""
        super().__init__()

    def move_to_end(self, key):
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value

    def put(self, key, item):
        """ Add an item in the cache
        """

        self.cache_data[key] = item
        self.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f'DISCARD: {list(self.cache_data.keys())[0]}')
            del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """ Get an item by key
        """
        if not key or key not in self.cache_data:
            return None
        self.move_to_end(key)
        return self.cache_data[key]
