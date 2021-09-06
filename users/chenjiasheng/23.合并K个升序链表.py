from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merge_lst = []
        for lst in lists:
            node = lst
            while node is not None:
                merge_lst.append(node.val)
                node = node.next
        merge_lst = sorted(merge_lst)
        nodes = [ListNode(x, None) for x in merge_lst]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if len(nodes) == 0:
            return None

        return nodes[0]