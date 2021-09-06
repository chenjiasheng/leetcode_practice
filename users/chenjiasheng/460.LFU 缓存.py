from typing import Dict, Set, List, Tuple
import bisect



class SortedList:
    def __init__(self):
        self.lst = []

    def add(self, elem):
        bisect.insort_left(self.lst, elem)

    def remove(self, elem):
        del self.lst[bisect.bisect_left(self.lst, elem)]

    def __getitem__(self, index):
        return self.lst[index]

    def __delitem__(self, index):
        del self.lst[index]


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, List[int, int, int]] = {}
        self.sorted_list: SortedList[Tuple[int, int, int]] = SortedList()
        self.timestamp = 0

    def get(self, key: int) -> int:
        self.timestamp += 1
        if key not in self.cache:
            return -1
        value, use_count, last_time = self.cache[key]
        self.cache[key][1] += 1
        self.cache[key][2] = self.timestamp
        self.sorted_list.remove([use_count, last_time, key])
        self.sorted_list.add([use_count + 1, self.timestamp, key])
        return value

    def _put_new(self, key, value):
        self.cache[key] = [value, 1, self.timestamp]
        self.sorted_list.add([1, self.timestamp, key])

    def put(self, key: int, value: int) -> None:
        self.timestamp += 1
        if self.capacity == 0:
            return
        if key in self.cache:
            old_value, use_count, last_time = self.cache[key]
            self.cache[key] = [value, use_count + 1, self.timestamp]
            self.sorted_list.remove([use_count, last_time, key])
            self.sorted_list.add([use_count + 1, self.timestamp, key])
        else:
            if len(self.cache) < self.capacity:
                self._put_new(key, value)
            else:
                use_count, last_time, old_key = self.sorted_list[0]
                del self.sorted_list[0]
                del self.cache[old_key]
                self._put_new(key, value)
