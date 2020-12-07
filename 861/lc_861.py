import numpy as np


class Solution:
    def matrixScore(self, A):
        A = np.array(A)
        # 对于每一行，如果第一位非1，则翻转这一行
        for i, row in enumerate(A):
            if row[0] != 1:
                A[i] = 1 - row

        # 对于每一列，如果这列0的个数大于1的个数则翻转这一列
        A = A.transpose()
        half = len(A[0]) / 2
        for i, colum in enumerate(A):
            if np.sum(colum) < half:
                A[i] = 1 - colum

        # 统计分数
        A = A.transpose()
        score_sum = 0
        for row in A:
            bin_value = ''.join(list(map(str, row)))
            score_sum += int(bin_value, base=2)
        return score_sum


if __name__ == '__main__':
    A = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    a = Solution()
    res = a.matrixScore(A)
    print(res)
