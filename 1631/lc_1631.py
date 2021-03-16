from queue import PriorityQueue
import numpy as np

# 解题思路同778，均采用dijkstra算法
class compareAble():
    def __init__(self, effort, pos):
        self.effort = effort
        self.pos = pos

    def __lt__(self, other):
        if self.effort < other.effort:
            return True
        else:
            return False


class Solution:
    def is_area(self, pos):
        return pos[0] < self.rows and pos[0] >= 0 and pos[1] < self.column and pos[1] >= 0

    def near_pos(self, pos):
        moves = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
        pos = np.array(pos)
        near_pos = []
        for m in moves:
            near_pos.append(m + pos)
        return near_pos

    def minimumEffortPath(self, heights):
        max_height = 10 ** 6 + 1
        rows = len(heights)
        column = len(heights[0])
        self.rows = rows
        self.column = column
        visit = [[0 for _ in range(column)] for _ in range(rows)]
        pq = PriorityQueue()
        pq.put(compareAble(0, (0, 0)))
        dist = [[max_height for _ in range(column)] for _ in range(rows)]
        dist[0][0] = 0
        while pq.qsize():
            cur = pq.get()
            cur_pos = cur.pos
            visit[cur_pos[0]][cur_pos[1]] = 1

            if cur_pos[0] == rows-1 and cur_pos[1] == column-1:
                return dist[cur_pos[0]][cur_pos[1]]

            for next in self.near_pos(cur_pos):
                if self.is_area(next):
                    effort = max(abs(
                        heights[cur_pos[0]][cur_pos[1]] - heights[next[0]][
                            next[1]]), dist[cur_pos[0]][cur_pos[1]])
                    if effort < dist[next[0]][next[1]]:
                        dist[next[0]][next[1]] = effort
                        pq.put(compareAble(effort, (next[0], next[1])))


if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    solve = Solution()
    res = solve.minimumEffortPath(heights)
    print(res)
