# 每日一题：62 不同路径

这道题主要考察排列组合，没啥难度。看懂题目想要干啥，就能做出来。

高中数学学得好，算法刷题没烦恼～



关键字： `排列组合`

## 题目

Leetcode62.[不同路径](https://leetcode-cn.com/problems/unique-paths/)

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

![problem](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

示例 1：

```
输入：m = 3, n = 7
输出：28
```

## 题解

从左上角走到右下角，只能向下、向右走。以上图为例，左上到右下，一共需要走（3-1）+（7-1）=8步，从这8步中选定向下的2步，那么向右的6步也随之确定。并且这向下的两步是无序的，所以套用组合的公式求解即可。

这里给大家复习一下**排列组合公式：**

**排列**：从n个物品中，按顺序选择k个物品，选择方式有$A(n,k)=\frac{n!}{(n-k)!}$ 种。

**组合**：从n个物品中，选择k个物品，选择方式有$C(n,k)=\frac{n!}{(n-k)!k!}$ 种。

### Python 实现

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 一共要走的步数
        total_path = m + n - 2
        # 向下或者向右的步数，这里选择小的那个是为了循环计算阶乘时减少计算
        choice = min(m, n)-1
        # 分子 n！/(n-k)!
        res = 1
        # 分母 k！
        repeat = 1
        for i in range(choice):
            res = res * (total_path - i)
            repeat = repeat * (i + 1)
        return int(res / repeat)
```


