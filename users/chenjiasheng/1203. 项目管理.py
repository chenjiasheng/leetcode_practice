from typing import List
from collections import defaultdict


def topo_sort(items, dependence_dict):
    if len(items) == 1:
        return items

    n = len(items)
    item_to_idx = {item: idx for idx, item in enumerate(items)}
    adj = defaultdict(list)
    for item, lst in dependence_dict.items():
        if item not in item_to_idx:
            continue
        v = item_to_idx[item]
        for item2 in lst:
            if item2 not in item_to_idx:
                continue
            u = item_to_idx[item2]
            adj[u].append(v)

    roots = set(range(n))
    for u in adj:
        for v in adj[u]:
            if v in roots:
                roots.remove(v)

    white, gray, black = 0, 1, 2
    colors = [white] * n
    sorted_indices = []
    def dfs(u):
        if colors[u] == black:
            return
        if colors[u] == gray:
            raise RuntimeError
        colors[u] = gray
        for v in adj[u]:
            dfs(v)
        sorted_indices.append(u)
        colors[u] = black
    for root in roots:
        dfs(root)
    sorted_indices = sorted_indices[::-1]
    if len(sorted_indices) != n:
        raise RuntimeError
    return [items[i] for i in sorted_indices]


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for i, g in enumerate(group):
            groups[g].append(i)
        extra_group_id = m
        for i in groups[-1]:
            groups[extra_group_id] = [i]
            extra_group_id += 1
        groups.pop(-1)
        id_to_group = [-1] * n
        for g, lst in groups.items():
            for i in lst:
                id_to_group[i] = g

        def topological_sort_inner():
            beforeItemsDict = {i: lst for i, lst in enumerate(beforeItems) if len(lst) != 0}
            for g in groups:
                groups[g] = topo_sort(groups[g], beforeItemsDict)

        try:
            topological_sort_inner()
        except RuntimeError:
            return []

        def topological_sort_outer():
            beforeGroupIds = defaultdict(set)
            for i, lst in enumerate(beforeItems):
                g1 = id_to_group[i]
                for j in lst:
                    g2 = id_to_group[j]
                    if g1 != g2:
                        beforeGroupIds[g1].add(g2)
            return topo_sort(list(groups.keys()), beforeGroupIds)

        try:
            group_ids = topological_sort_outer()
        except RuntimeError:
            return []

        if len(group_ids) != len(groups):
            return []

        result = [i for g in group_ids for i in groups[g]]
        return result

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(Solution().sortItems(n, m, group, beforeItems))


n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
print(Solution().sortItems(n, m, group, beforeItems))


