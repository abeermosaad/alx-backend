#!/usr/bin/env python3
""" Simple pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """ Return a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = 'Popular_Baby_Names.csv'

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get the page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if self.dataset():
            return self.__dataset[start_index: end_index]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> {}:
        """ Get the page of the dataset with hypermedia pagination
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if self.dataset():
            dic = {}
            dic.update({
                'page_size': len(self.__dataset[start_index: end_index]),
                'page': page,
                'data': self.__dataset[start_index: end_index],
                'next_page': page + 1 if end_index < len(self.__dataset)
                else None,
                'prev_page': page - 1 if start_index > 0 else None,
                'total_pages': math.ceil(len(self.__dataset) / page_size)
            })
        return dic
