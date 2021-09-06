from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        splits = [nodes[start_index:start_index+k] for start_index in range(0, len(nodes), k)]
        reversed_splits = [x[::-1] if len(x) == k else x for x in splits]
        reversed_k_group = [x for split in reversed_splits for x in split]
        for i in range(len(reversed_k_group) - 1):
            reversed_k_group[i].next = reversed_k_group[i + 1]
        reversed_k_group[-1].next = None
        return reversed_k_group[0]


def make_list(lst):
    if len(lst) == 0:
        return None

    nodes = [ListNode(x, None) for x in lst]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

head = make_list([1, 2])
k = 2
print(Solution().reverseKGroup(head, k))
