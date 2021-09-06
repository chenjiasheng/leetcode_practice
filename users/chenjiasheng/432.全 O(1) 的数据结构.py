from typing import List, Dict, Set
from collections import defaultdict
from sortedcontainers import SortedList

class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_count: Dict[str, int] = {}
        self.sorted_list = SortedList()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.key_to_count:
            self.key_to_count[key] = 1
            self.sorted_list.add((1, key))
        else:
            count = self.key_to_count[key]
            self.key_to_count[key] += 1
            self.sorted_list.remove((count, key))
            self.sorted_list.add((count + 1, key))

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_to_count:
            return
        count = self.key_to_count[key]
        if count == 1:
            del self.key_to_count[key]
            self.sorted_list.remove((count, key))
        else:
            self.key_to_count[key] -= 1
            self.sorted_list.remove((count, key))
            self.sorted_list.add((count - 1, key))

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if len(self.sorted_list) == 0:
            return ""

        return self.sorted_list[-1][1]

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if len(self.sorted_list) == 0:
            return ""

        return self.sorted_list[0][1]


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.inc("hello")
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc("leet")
print(obj.getMaxKey())
print(obj.getMinKey())
