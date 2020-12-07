# 翻转矩阵求值

今天的题太简单了。。。。随便写写题解～

## 题目

861题[翻转矩阵后的得分](https://leetcode-cn.com/problems/score-after-flipping-matrix/)

*题目描述*

有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

*例如*：

    输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    输出：39
    解释：
    转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
    0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


*提示*：

    1 <= A.length <= 20
    1 <= A[0].length <= 20
    A[i][j] 是 0 或 1

## 题解

本题的目的是获得尽可能高的分数，每一行当做一个二进制数，所以：
1. 对于每一行，第一个数字需要是1，如果不是1就翻转。
2. 对于每一列，每个值对于总分的贡献是一样的，所以，如果1的个数少于0的个数就翻转。

对矩阵A，行遍历一次，列遍历一次搞定，然后算个分数就ok了～

## 代码

```python
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
```

