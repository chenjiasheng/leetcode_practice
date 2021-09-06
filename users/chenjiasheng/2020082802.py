# http://3ms.huawei.com/km/groups/3803117/blogs/details/8891395?l=zh-cn

from typing import Dict, List, Tuple, Optional


def sell(init_goods: List[int],
         init_coins: List[int],
         purchase_list: List[Tuple[int, List[int]]]
         ) -> Tuple[bool, List[int]]:
    prices = [2, 3, 4, 5, 8, 6]
    coin_values = [1, 2, 5, 10]

    remain_goods = init_goods.copy()
    remain_coins = init_coins.copy()

    def give_change(coins, change: int) -> Optional[List[int]]:
        if change == 0:
            return [0, 0, 0, 0]

        sum_coins = sum(coins[i] * coin_values[i] for i in range(4))
        if sum_coins == change:
            return coins
        elif sum_coins < change:
            return None

        coins_ids = [i for i in range(4) if coins[i] > 0 and coin_values[i] <= change]
        if not coins_ids:
            return None

        i = max(coins_ids)
        j = change // coin_values[i]
        for k in range(j, -1, -1):
            change_coins = give_change(coins[:i] + [0] * (4 - i), change - k * coin_values[i])
            if change_coins is not None:
                return change_coins[:i] + [k] + [0] * (3 - i)
        return None

    def abandon_deal(change):
        change_coins = give_change(remain_coins, change)
        assert change_coins is not None
        for i in range(4):
            remain_coins[i] -= change_coins[i]
        return change_coins

    def apply_deal(change_coins):
        remain_goods[good_id] -= 1
        for i in range(4):
            remain_coins[i] -= change_coins[i]

    def deal(good_id, payment_coins):
        for i in range(4):
            remain_coins[i] += payment_coins[i]

        # abandon deal
        payment = sum(payment_coins[i] * coin_values[i] for i in range(4))
        if remain_goods[good_id] == 0 or payment < prices[good_id]:
            return False, abandon_deal(payment)

        # try deal
        try_change = payment - prices[good_id]
        change_coins = give_change(remain_coins, try_change)
        if change_coins is None:
            return False, abandon_deal(payment)

        apply_deal(change_coins)
        return True, change_coins

    result = None
    for good_id, payment_coins in purchase_list:
        result = deal(good_id, payment_coins)

    return result
