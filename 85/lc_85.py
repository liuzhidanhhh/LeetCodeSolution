import numpy as np


class Solution:
    def largestRectangleArea(self, heights):
        heights.insert(0, -1)
        heights.append(-1)
        stack = [0]  # 栈中存储height的index，每个位置的高度用height[index]求
        index = 1
        max_area = 0
        # 终止条件： 栈中只剩下哨兵，并且height遍历完
        while len(stack) > 1 or index < len(heights) - 1:
            # 当前元素大于栈顶元素时，进栈
            if heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            # 当前元素小于栈顶元素时，栈顶元素出栈，计算高度为栈顶元素高度时的面积
            elif heights[index] < heights[stack[-1]]:
                top = stack.pop()
                area = heights[top] * (index - stack[-1] - 1)
                if area > max_area:
                    max_area = area
        return max_area

    def maximalRectangle(self, matrix):
        matrix = np.array(matrix, dtype=int)
        N = len(matrix)
        if N == 0:
            return 0
        M = len(matrix[0])
        max_area = 0
        for i in range(1, N + 1):
            heights = []
            for j in range(M):
                h = 0
                for k in range(i - 1, -1, -1):
                    if matrix[k][j] == 0:
                        break
                    else:
                        h += 1
                heights.append(h)

            area = self.largestRectangleArea(heights)
            if area > max_area:
                max_area = area
        return int(max_area)


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    matrix = [["1", "0", "1", "1", "1"],
              ["0", "1", "0", "1", "0"],
              ["1", "1", "0", "1", "1"],
              ["1", "1", "0", "1", "1"],
              ["0", "1", "1", "1", "1"]]

    # matrix =[[0,1],[1,0]]
    solve = Solution()
    res = solve.maximalRectangle(matrix)
    print(res)
