from queue import Queue
import numpy as np


# 多源广搜队列度优先搜索， 所有的腐烂橘子为初始搜索队列
class Solution:
    def is_end(self, grid):
        res = np.where(np.array(grid) == 1)
        if res[0].size == 0:
            return True
        else:
            return False

    def is_area(self, pos):
        return pos[0] >= 0 and pos[0] < self.N and pos[1] >= 0 and pos[1] < self.M

    def can_moves(self, pos):
        pos = np.array(pos)
        moves = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
        return [pos + m for m in moves]

    def orangesRotting(self, grid):
        self.N = len(grid)
        self.M = len(grid[0])
        q = Queue()
        if self.is_end(grid):
            return 0

        rows, colums = np.where(np.array(grid) == 2)
        if rows.size == 0:
            return -1

        for r, c in zip(rows, colums):
            q.put(((r, c), 0))
        time = 0
        while q.qsize():
            pos, time = q.get()
            for m in self.can_moves(pos):
                if self.is_area(m) and grid[m[0]][m[1]] == 1:
                    grid[m[0]][m[1]] = 2
                    q.put((m, time + 1))

        if self.is_end(grid):
            return time
        else:
            return -1


if __name__ == '__main__':
    grid = [[0, 2]]
    solve = Solution()
    res = solve.orangesRotting(grid)
    print(res)
