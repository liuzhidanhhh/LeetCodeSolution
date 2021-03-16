from collections import defaultdict
from queue import Queue


class Solution:
    def shortestPathLength(self, graph):
        N = len(graph)
        queue = Queue()
        for i in range(N):
            queue.put((1 << i, i))
        # 无环图最多有N（N-1)/2条边，为什么这里设的默认最大值为N×N？
        dist = defaultdict(lambda: N * N)
        # 从每个点出发的初始距离均为0
        for i in range(N):
            dist[1 << i, i] = 0
        while queue.qsize():
            cover, cur = queue.get()

            # 终止条件:
            if cover == (1 << N )- 1:
                return dist[cover, cur]

            for child in graph[cur]:
                new_cover = cover | (1 << child)
                if dist[cover, cur] + 1 < dist[new_cover, child]:
                    dist[new_cover, child] = dist[cover, cur] + 1
                    queue.put((new_cover, child))


if __name__ == '__main__':
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    solve = Solution()
    res = solve.shortestPathLength(graph)
    print(res)
