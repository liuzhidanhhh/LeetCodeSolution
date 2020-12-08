import math


class Solution:
    def splitIntoFibonacci(self, S):
        S = list(S)
        res = []    # 存储分割后的序列，序列始终满足斐波那契序列
        max_value = math.pow(2, 31) - 1
        if len(S) < 3:
            return []

        def backtrace(i):
            # 终止条件，当到达序列的末尾，并且分割后的序列中元素大于三个
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


if __name__ == '__main__':
    a = Solution()
    s = "0123"
    res = a.splitIntoFibonacci(s)
    print(res)
