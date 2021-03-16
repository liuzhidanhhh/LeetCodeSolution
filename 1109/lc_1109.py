import numpy as np


class Solution:
    def corpFlightBookings(self, bookings, n):
        res = np.zeros(n,int)
        for book in bookings:
            res[book[0]-1:book[1]] += book[2]
        return res


if __name__ == '__main__':
    solve = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    res = solve.corpFlightBookings(bookings,n)
    print(res)