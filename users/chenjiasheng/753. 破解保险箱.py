import math


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(str(i) for i in range(k))
        if k == 1:
            return '0' * n

        def edge_id(lst):
            node = 0
            for x in lst:
                node *= k
                node += x
            return node

        back_track = []
        visited = [False] * int(math.pow(k, n))

        def dfs(node):
            #print(node)
            for i in range(k):
                edge = node + [i]
                edge_id = edge_id(edge)
                if not visited[edge_id]:
                    next_node = edge[1:]
                    visited[edge_id] = True
                    dfs(next_node)
            back_track.append(node)

        dfs([0] * (n-1))
        node_lst = back_track[::-1]
        #print([x for x in node_lst])
        res = ''
        for x in node_lst[0][1:]:
            res += str(x)
        for node in node_lst:
            res += str(node[-1])
        return res



solution = Solution()
xx = solution.crackSafe(1, 2)
print(xx)
print(len(xx))

