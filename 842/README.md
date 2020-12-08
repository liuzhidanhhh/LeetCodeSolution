# LeetCode 每日一题： 842. 将数组拆分成斐波那契序列

今天这道题考察的是：`深度优先回溯算法`，回溯算法有一套算法模板，关于回溯算法的讲解可以[参考这篇文章](https://zhuanlan.zhihu.com/p/93530380)

代码： https://github.com/liuzhidanhhh/LeetCodeSolution/blob/master/842/lc_842.py

## 题目描述

给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。

形式上，斐波那契式序列是一个非负整数列表 F，且满足：

1. <font color=green> 0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型；</font>
2. <font color=blue> F.length >= 3; </font>
3. <font color=blue> 对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。 </font>

另外，请注意，<font color=green>将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身</font>。

返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

示例 1：

    输入："123456579"
    输出：[123,456,579]

提示：

    1 <= S.length <= 200
    字符串 S 中只含有数字。

## 题解

在解决这个问题之前，我们先回顾一下回溯算法。回溯算法本质上是一个决策树的遍历过程，在这个遍历过程中主要考虑3个元素：

1. 路径：已经走过的路径
2. 选择列表：当前可以做的选择
3. 结束条件：搜索到决策树的底层，无法继续搜索
4. 其他，在具体算法过程中，可以使用的剪枝条件

**回溯算法模板**

    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)842

backtrack()递归过程是在做DFS的搜索， for循环是当前层的遍历，在for循环内做选择与撤销选择是在回溯。



现在，我们用这道题目来感受一下回溯算法。借用leetcode的`数据结构与算法`的[题解](https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/solution/javahui-su-suan-fa-tu-wen-xiang-jie-ji-b-vg5z/)中的一张图片来说明DFS回溯与剪枝过程：

对于给定数字字符串S="124557"，DFS回溯搜索过程如下图：

![image.png](https://pic.leetcode-cn.com/1607416979-Gqmezs-image.png)

**终止条件**：整个字符串搜索完

**剪枝条件**：题目描述中绿色字体部分是两个明显的剪枝条件

	1.  F[i] > 2^31 - 1，如果分割的数字超过这个限制值
 	2.  0x类型数字，非0数字，以0开头

第三个剪枝条件从上图可以看出，如果F(n)>F(n-1)+F(n-2)那么接下来的划分都会超过F(n)

3. F(n)>F(n-1)+F(n-2)



**Python实现**

```python
import math


class Solution:
    def splitIntoFibonacci(self, S):
        S = list(S)
        res = []    # 存储分割后的序列，序列始终满足斐波那契序列
        max_value = math.pow(2, 31) - 1
        if len(S) < 3:
            return []

        def backtrace(i):
            # 终止条件，当到达序列的末尾
            if i == len(S):
                return len(res) >= 3

            cur_value = 0
            for j in range(i, len(S)):
                # 剪枝条件1: 0x类型数据
                if S[i] == '0' and j > i:
                    break

                cur_value = cur_value * 10 + int(S[j])
                # 剪枝条件2: 数据值 > 2^31-1
                if cur_value > max_value:
                    break

                # 剪枝条件3: 如果f(n)>f(n-2)+f(n-1)
                if len(res) >= 2 and cur_value > res[-1] + res[-2]:
                    break

                if len(res) < 2 or cur_value == res[-1] + res[-2]:
                    # 当前分割，满足斐波那契，进队
                    res.append(cur_value)
                    # DFS 搜索剩余的序列
                    if backtrace(j + 1):
                        return True
                    # 撤销
                    res.pop()
            return False

        backtrace(0)

        return res
```