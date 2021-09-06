""" http://3ms.huawei.com/km/groups/3803117/blogs/details/9583356?l=zh-cn """

from collections import defaultdict
from typing import List


def stat_greater(iterable, n):
    stat = defaultdict(int)
    for x in iterable:
        stat[x] += 1
    sorted_values = sorted(stat.keys())
    grater_stat = defaultdict(int)
    accumulate = 0
    for value in sorted_values:
        accumulate += stat[value]
        grater_stat[value] = n - accumulate
    return grater_stat


def solve(scores: List[List[int]]):
    rows, cols = len(scores), len(scores[0])
    stat_by_row = [stat_greater(row, cols) for row in scores]
    stat_by_col = [stat_greater(col, rows) for col in zip(*scores)]
    result = [[stat_by_row[i][scores[i][j]] + stat_by_col[j][scores[i][j]]
               for j in range(cols)] for i in range(rows)]
    return result


scores = [[10, 20, 30], [30, 15, 10]]
print(solve(scores))
