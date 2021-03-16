from queue import Queue


class Solution:
    def can_move(self, x, y):
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        for m in moves:
            if x + m[0] >= 0 and x + m[0] < self.m and y + m[1] >= 0 and y + m[
                1] < self.n:
                res.append([x + m[0], y + m[1]])
        return res

    def shortestPath(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0
        k = min(k, m + n - 3)
        self.m, self.n = m, n
        q = Queue()
        q.put((0, 0, k, 0))
        visit = [[[False for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
        visit[0][0][k] = True
        while q.qsize():
            x, y, rest, path = q.get()
            if x == m - 1 and y == n - 1:
                return path
            for new_x, new_y in self.can_move(x, y):
                if grid[new_x][new_y] == 1:
                    if rest - 1 >= 0:
                        if not visit[new_x][new_y][rest - 1]:
                            visit[new_x][new_y][rest-1]=True
                            q.put((new_x, new_y, rest - 1, path + 1))
                else:
                    if not visit[new_x][new_y][rest]:
                        visit[new_x][new_y][rest] = True
                        q.put((new_x, new_y, rest, path + 1))
        return -1


if __name__ == '__main__':
    # grid = [[0, 0, 0],
    #         [1, 1, 0],
    #         [0, 0, 0],
    #         [0, 1, 1],
    #         [0, 0, 0]]
    # k = 1
    # grid = [[0, 1, 1],
    #         [1, 1, 1],
    #         [1, 0, 0]]
    # k = 1
    # grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    #         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    #         [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    #         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    #         [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    # k = 1
    grid = [[0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 1],
            [0, 1], [0, 1], [0, 0], [1, 0], [1, 0], [0, 0]]
    k = 4
    solve = Solution()
    res = solve.shortestPath(grid, k)
    print(res)
