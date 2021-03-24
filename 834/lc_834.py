import numpy as np


class Solution:
    def sumOfDistancesInTree(self, N, edges):
        dist = np.zeros((N, N), dtype=int)
        for e in edges:
            dist[e[0]][e[1]] = 1
            dist[e[1]][e[0]] = 1

        for i in range(N):
            for j in range(i + 1, N):
                if dist[i][j] > 0:
                    continue

        res = np.sum(dist, axis=1)
        return list(res)



if __name__ == '__main__':
    N = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    solve = Solution()
    res = solve.sumOfDistancesInTree(N, edges)
    print(res)
