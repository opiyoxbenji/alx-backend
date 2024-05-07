#!/usr/bin/env python3
"""
Task 3 - Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        gets info of a page from a specified index
        """
        data_set = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(
                data_set.keys())
        data_p = []
        counter = 0
        next_idx = None
        starting = index if index else 0
        for a, item in data_set.items():
            if a >= starting and counter < page_size:
                data_p.append(item)
                counter += 1
                continue
            if counter == page_size:
                next_idx = a
                break
        info = {
            'index': index,
            'next_index': next_idx,
            'page_size': len(data_p),
            'data': data_p,
        }
        return info
