import numpy as np


class Solution:
    def pondSizes(self, land):
        result = []
        pool = []
        searched = np.zeros(np.shape(land), int)
        n = len(land)
        m = len(land[0])

        def seach_neighbor(x, y):
            neighor = [-1, 0, 1]
            pool_pos = []
            for n1 in neighor:
                for n2 in neighor:
                    new_x = x + n1
                    new_y = y + n2
                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or \
                            land[new_x][new_y] == '#':
                        continue
                    if land[new_x][new_y] == 0:
                        land[new_x][new_y] = '#'
                        pool_pos.append((x + n1, y + n2))
                    else:
                        land[new_x][new_y] = '#'
            return pool_pos

        for x in range(n):
            for y in range(m):
                if land[x][y] == 0:
                    land[x][y] = '#'
                    pool.append((x, y))
                    pool_nei = seach_neighbor(x, y)
                    pool = pool + pool_nei
                    while pool_nei:
                        x, y = pool_nei.pop()
                        new_nei = seach_neighbor(x, y)
                        if new_nei:
                            pool_nei = pool_nei + new_nei
                            pool = pool + new_nei
                    result.append(pool)
                    pool=[]
                else:
                    land[x][y] = '#'

        result_num = [len(res) for res in result]
        return sorted(result_num)


if __name__ == '__main__':
    solve = Solution()
    land = [[0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]]
    res = solve.pondSizes(land)
    print(res)