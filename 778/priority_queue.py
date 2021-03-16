from queue import PriorityQueue
import numpy as np


class compareAble:
    def __init__(self, weight, positation):
        self.weight = weight
        self.positataion = positation

    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        else:
            return False

# dijkstra
# 非负权单源最短路径问题
# 权重为grid[x][y]
class Solution:
    def is_area(self, pos):
        return pos[0] >= 0 and pos[0] < self.N and pos[1] >= 0 and pos[
            1] < self.N

    def near_area(self, pos):
        pos = np.array(pos)
        moves = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
        new_pos = []
        for m in moves:
            new = pos + m
            new_pos.append(new)

        return new_pos

    def swimInWater(self, grid):
        # 初始化
        pq = PriorityQueue()
        N = len(grid)
        self.N = N
        visit = np.zeros((N, N))
        dist = [[N*N for _ in range(N)] for _ in range(N)]
        pq.put(compareAble((grid[0][0]), (0, 0)))
        dist[0][0] = grid[0][0]

        while (pq.qsize()):
            # 从优先队列中找到最短路径点
            cur = pq.get()
            cur_pos = cur.positataion
            visit[cur_pos[0]][cur_pos[1]] = 1

            # 判断终止条件
            if cur_pos[0] == N - 1 and cur_pos[1] == N - 1:
                return dist[N-1][N-1]

            # 更新
            for new in self.near_area(cur_pos):
                # 当前点u的所有可达点news中，在矩阵边界范围内的点
                if self.is_area(new):
                    # 如果 max(源点到new的最短路径，grid)< dist[new]，则这条源点到new的距离更短，更新
                    pro_dist = max(grid[new[0]][new[1]], dist[cur_pos[0]][cur_pos[1]])
                    if pro_dist < dist[new[0]][new[1]]:
                        dist[new[0]][new[1]] = pro_dist
                        # 可达点入队
                        pq.put(compareAble(pro_dist, (new[0], new[1])))


if __name__ == '__main__':
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    solve = Solution()
    res = solve.swimInWater(grid)
    print(res)
