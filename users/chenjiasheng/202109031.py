from typing import List
from collections import deque


class Question1:
    """
    题目一：销售方案
    有n件商品的列表sales，其中每件商品用三元组<_type, cost, profit>表示，
    请按照成本最小、利润最大和种类最小的原则，从其中挑选出cnt件商品出来，且须满足以下限制条件：
    limit是一列表，其每个元素是一个二元组<_type, limit_cnt>，
    表示种类为type的商品至多挑选limit_cnt件
    """
    def getSalesSolution(self,
                         sales: List[List[int]],
                         cnt: int,
                         limit: List[List[int]]) -> List[int]:
        sorted_indices = sorted(
            range(len(sales)),
            key=lambda i: (sales[i][1], -sales[i][2], sales[i][0]))
        limit_map = {x[0]: x[1] for x in limit}

        result = []
        for index in sorted_indices:
            if len(result) >= cnt:
                break
            _type, cost, profit = sales[index]
            if limit_map[_type] <= 0:
                continue
            limit_map[_type] -= 1
            result.append(index)

        if len(result) < cnt:
            return []
        return result

