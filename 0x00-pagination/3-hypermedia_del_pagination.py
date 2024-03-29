#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, any]:
        """ Get the page of the dataset with hypermedia pagination
        """
        assert index >= 0 and index < len(self.__indexed_dataset)
        dic, li, cnt, i, idx = {}, [], 0, index, 0
        while cnt < page_size:
            if i in self.__indexed_dataset:
                cnt += 1
                li.append(self.__indexed_dataset[i])
            else:
                idx += 1
            i += 1

        dic.update({
            'index': index,
            'data': li,
            'page_size': page_size,
            'next_index': index + page_size + idx
            if index + page_size + idx < len(self.__indexed_dataset) else None,
        })
        return dic
