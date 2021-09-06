""" 题目二：订票系统
实现订票系统的以下接口：
init: 给定每种票（头等舱、一等舱、二等舱...）的初始票数cab_seat_nums，初始化订票系统
book: 订票。订单号book_id，预定cab等级的票num张。系统保证book_id全局唯一。
    如果该种票数不够，则把订单book_id加入cab仓的等待队列中排队，并返回false。
    如果票数足够，优先分配连号的座位号最小的num张票，如果不存在连号的票，
    则分配座位号最小的num张票。返回分配的票中，最小的票的座位号
cancel: 取消订单，订单号是book_id.
    如果该订单已经成功预定，则取消该订单，释放为其分配的座位。
    如果该订单是队列中的订单，则从队列中删除之。
    cancel成功之后，要对队列重新分票。
    如果该订单不存在，返回false，否则返回true。
query: 查询订单book_id的最小座位号。
    如果订单不存在或在等待队列中，返回-1
    如果订单已经预定成功，返回其最小编号座位的编号
"""

from typing import List, Tuple


class Solution:
    class TicketSystem:
        def __init__(self, cab_seat_nums: List[int]):
            self.seat_bitmap: dict[int, List[int]] = {
                cab: ([1] * seat) for cab, seat in enumerate(cab_seat_nums)}
            self.ordered_map: dict[int, Tuple[int, List[int]]] = {}
            self.wait_queues: List[List[int]] = list(
                [] for _ in range(len(cab_seat_nums)))
            self.wait_map: dict[int, Tuple[int, int]] = {}

        def _can_assign(self, cab, num):
            remain_seat = sum(self.seat_bitmap[cab])
            return remain_seat >= num

        def _enqueue(self, book_id, cab, num):
            self.wait_queues[cab].append(book_id)
            self.wait_map[book_id] = (cab, num)

        def _dequeue(self, book_id):
            cab, num = self.wait_map.get(book_id)
            self.wait_queues[cab].remove(book_id)
            del self.wait_map[book_id]

        def _get_seats(self, cab, num):
            book_seats = []
            i = 0
            while i < len(self.seat_bitmap[i]) and self.seat_bitmap[i] != 1:
                i += 1

            while i < len(self.seat_bitmap[i]):
                if sum(self.seat_bitmap[cab][i: i + num]) == num:
                    book_seats.extend(range(i, i + num))
                    break
                while i < len(self.seat_bitmap[i]) and self.seat_bitmap[i] == 1:
                    i += 1
                while i < len(self.seat_bitmap[i]) and self.seat_bitmap[i] == 0:
                    i += 1
                if i >= len(self.seat_bitmap[i]):
                    break

            if len(book_seats) == 0:
                for i in range(len(self.seat_bitmap[cab])):
                    if self.seat_bitmap[cab][i] == 1:
                        book_seats.append(i)
                    if len(book_seats) == num:
                        break
            return book_seats

        def _assign_seats(self, book_id, cab, seats):
            for seat in seats:
                self.seat_bitmap[cab][seat] = 0
            self.ordered_map[book_id] = (cab, seats)

        def _release_seats(self, book_id):
            cab, book_seats = self.ordered_map.get(book_id)
            for seat in book_seats:
                self.seat_bitmap[cab][seat] = 1
            del self.ordered_map[book_id]

        def book(self, book_id: int, cab: int, num: int) -> bool:
            if (len(self.wait_queues[cab]) > 0
                    or not self._can_assign(cab, num)):
                self._enqueue(book_id, cab, num)
                return False

            seats = self._get_seats(cab, num)
            self._assign_seats(book_id, cab, seats)
            return True

        def cancel(self, book_id: int) -> bool:
            if (book_id not in self.ordered_map
                    and book_id not in self.wait_map):
                return False

            cab = None
            if book_id in self.wait_map:
                cab, _ = self.wait_map.get(book_id)
                self._dequeue(book_id)
            elif book_id in self.ordered_map:
                cab, _ = self.ordered_map.get(book_id)
                self._release_seats(book_id)

            while len(self.wait_queues[cab]) != 0:
                wait_book_id = self.wait_queues[cab][0]
                wait_cab, wait_num = self.wait_map.get(wait_book_id)
                if not self._can_assign(cab, wait_num):
                    break
                self._dequeue(wait_book_id)
                seats = self._get_seats(cab, wait_num)
                self._assign_seats(wait_book_id, cab, seats)

            return True

        def query(self, book_id: int) -> int:
            if book_id not in self.ordered_map:
                return -1

            return self.ordered_map.get(book_id)[1][0]


if __name__ == '__main__':
    tiket_system = Solution.TicketSystem([10, 1])
    print(tiket_system.book(71, 0, 2))  # true
    print(tiket_system.book(73, 0, 10))  # false
    print(tiket_system.book(72, 0, 2))  # false
    print(tiket_system.query(72))  # -1
    print(tiket_system.book(74, 0, 2))  # false
    print(tiket_system.cancel(73))  # true
    print(tiket_system.query(74))  # 4
    print(tiket_system.query(72))  # 2
    print(tiket_system.cancel(72))  # true
    print(tiket_system.book(75, 0, 3))  # true
    print(tiket_system.query(75))  # 6
    print(tiket_system.cancel(75))  # true
    print(tiket_system.book(76, 0, 2))  # true
    print(tiket_system.book(77, 0, 2))  # true
    print(tiket_system.cancel(76))  # true
    print(tiket_system.book(78, 0, 3))  # true
    print(tiket_system.query(78))  # 2

