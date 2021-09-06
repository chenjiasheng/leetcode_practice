from collections import deque

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        cities = set()
        for s, t in tickets:
            cities.add(s)
            cities.add(t)
        cities = sorted(cities)
        cities_ids = {city:i for i, city in enumerate(cities)}
        n = len(cities)

        adjs = [list() for _ in range(n)]
        for s, t in tickets:
            adjs[cities_ids[s]].append(cities_ids[t])
        for s in range(n):
            adjs[s].sort(reverse=True)

        indegrees = [0] * n
        outdegrees = [0] * n
        for s in range(n):
            for t in adjs[s]:
                indegrees[t] += 1
                outdegrees[s] += 1
        source = -1
        target = -1
        for i in range(n):
            diff = indegrees[i] - outdegrees[i]
            if diff not in [-1, 0, 1]:
                return []
            if diff == 0:
                continue
            elif diff == -1:
                if source != -1:
                    return []
                else:
                    source = i
            else:
                if target != -1:
                    return []
                else:
                    target = i
        if source == -1 and target != -1 or source != -1 and target == -1:
            return []
        if source == -1 and target == -1:
            source = target = cities_ids['JFK']

        if source != cities_ids['JFK']:
            return []

        path = deque()
        def dfs_visit(u):
            while len(adjs[u]) != 0:
                v = adjs[u].pop()
                dfs_visit(v)
            path.appendleft(u)
        dfs_visit(source)

        result = [cities[u] for u in path]
        return result

tickets = [["SFO","JFK"],["SFO","ATL"],["JFK","ATL"],["ATL","SFO"],["ATL","JFK"]]
print(Solution().findItinerary(tickets))
