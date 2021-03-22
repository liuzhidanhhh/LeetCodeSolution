# DP
MaxV = 201


class Solution:
    def minFallingPathSum(self, arr):
        N = len(arr)
        value = [[0 for _ in range(N)] for _ in range(N)]
        value[0] = arr[0].copy()

        # 到达V(i,j)点的非零和路径最小值为：arr[i][j]+ min（V(i-1)中非零和列）
        for i in range(1, N):
            for j in range(N):
                tmp = value[i - 1].copy()
                tmp[j] = MaxV
                value[i][j] = arr[i][j] + min(tmp)
        # 终止条件： 最后一行的最小值为全局最小非零和路径
        return min(value[-1])


if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solve = Solution()
    res = solve.minFallingPathSum(arr)
    print(res)
