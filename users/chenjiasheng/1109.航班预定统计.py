from collections import defaultdict


class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = defaultdict(int)
        for first, last, seats in bookings:
            diff[first] += seats
            diff[last+1] -= seats

        result = [0] * (n+1)
        for i in range(1, n+1):
            result[i] = result[i-1] + diff[i]

        return result[1:]


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(Solution().corpFlightBookings(bookings, n))