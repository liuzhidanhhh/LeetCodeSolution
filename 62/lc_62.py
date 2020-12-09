class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_path = m + n - 2
        choice = min(m, n)-1
        res = 1
        repeat = 1
        for i in range(choice):
            res = res * (total_path - i)
            repeat = repeat * (i + 1)
        return int(res / repeat)


if __name__ == '__main__':
    solve = Solution()
    m = 7
    n = 3
    res = solve.uniquePaths(m, n)
    print(res)
