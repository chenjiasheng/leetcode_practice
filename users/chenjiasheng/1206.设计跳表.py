import random
from typing import List

MAX_VALUE = 20000
NUM_LAYERS = 15


class Skiplist:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next: List = [None] * NUM_LAYERS

        def __repr__(self):
            return str(self.val)

    def __init__(self):
        self.n_layers = 15
        self.head = Skiplist.Node(-1)
        self.tail = Skiplist.Node(MAX_VALUE + 1)
        for i in range(NUM_LAYERS):
            self.head.next[i] = self.tail

    def search(self, target: int) -> bool:
        path = self._search(target)
        if path is None:
            return False
        return path[-1].next[0].val == target

    def _search(self, num):
        path = []
        node = self.head
        layer = NUM_LAYERS - 1
        while True:
            if num > node.next[layer].val:
                if node.next[layer].val == MAX_VALUE + 1:
                    return None
                node = node.next[layer]
            else:
                path.append(node)
                if layer == 0:
                    return path
                layer -= 1

    def add(self, num: int) -> None:
        path = self._search(num)
        assert path is not None
        coin_flip_count = 0
        while coin_flip_count < NUM_LAYERS - 1 and random.randint(0, 1):
            coin_flip_count += 1
        new_node = Skiplist.Node(num)
        for layer in range(1 + coin_flip_count):
            prev = path[NUM_LAYERS - 1 - layer]
            next = prev.next[layer]
            prev.next[layer] = new_node
            new_node.next[layer] = next

    def erase(self, num: int) -> bool:
        path = self._search(num)
        if path is None:
            return False
        if path[-1].next[0].val != num:
            return False

        node = path[-1].next[0]
        for layer in range(NUM_LAYERS):
            prev = path[NUM_LAYERS - 1 - layer]
            if prev.next[layer] == node:
                prev.next[layer] = node.next[layer]
        return True


skiplist = Skiplist()
print(skiplist.add(1))
print(skiplist.add(2))
print(skiplist.add(3))
print(skiplist.search(0))
print(skiplist.add(4))
print(skiplist.search(1))
print(skiplist.erase(0))
print(skiplist.erase(1))
print(skiplist.search(1))
print(skiplist.add(1))
print(skiplist.erase(2))
print(skiplist.search(2))

