import numpy as np
from queue import Queue


class Solution:
    # 构图， 将一辆公交车的路线看成一个点，将起始点和终点也看成一个点，构一个无向图
    def make_graph(self, routes, source, target):
        num_routes = len(routes)
        graph = [[] for i in range(num_routes + 2)]
        for i in range(num_routes):
            for j in range(i + 1, num_routes):
                if self.is_connect(routes[i], routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)
            if source in routes[i]:
                graph[num_routes].append(i)
            if target in routes[i]:
                graph[i].append(num_routes + 1)

        return graph

    def is_connect(self, route1, route2):
        if set(route1) & set(route2):
            return True
        else:
            return False

    def numBusesToDestination(self, routes, source, target):
        # 构图， 将一辆公交车的路线看成一个点，将起始点s和终点t也看成点S，T，构一个无向图
        # 无向图上S到T的路径长度为所求最少搭乘公交车数量

        # 可用BFS搜索

        # 考虑边界情况，source=target
        if source == target:
            return 0
        num_routes = len(routes)
        graph = self.make_graph(routes, source, target)
        queue = Queue()
        # 队列存储，队列中指定点所在深度（node，depth）
        queue.put((num_routes, 0))  # node ,depth
        visited = [False for _ in range(num_routes + 2)]
        while queue.qsize():
            cur = queue.get()
            visited[cur[0]] = True
            nexts = graph[cur[0]]
            for n in nexts:
                if n == num_routes + 1:
                    return cur[1]
                if not visited[n]:
                    queue.put((n, cur[1] + 1))
        return -1


if __name__ == '__main__':
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    # routes = [[7, 12], [4, 5, 15], [6], [15, 19],
    #           [9, 12, 13]]
    # source = 15
    # target = 12
    # routes = [[1, 9, 12, 20, 23, 24, 35, 38],
    #           [10, 21, 24, 31, 32, 34, 37, 38, 43],
    #           [10, 19, 28, 37],
    #           [8],
    #           [14, 19],
    #           [11, 17, 23, 31, 41, 43, 44],
    #           [21, 26, 29, 33],
    #           [5, 11, 33, 41],
    #           [4, 5, 8, 9, 24, 44]]
    # source = 37
    # target = 28
    solve = Solution()
    res = solve.numBusesToDestination(routes, source, target)
    print(res)
