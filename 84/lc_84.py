# 加哨兵的单调站，题目中高度为非负，所以两端的哨兵可以为-1
# list 可以用于模拟栈
#
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


if __name__ == '__main__':
    # heights = [2, 1, 5, 6, 2, 3]
    # heights = [0,1,0,1]
    heights = [1, 1, 2, 2]

    solve = Solution()
    res = solve.largestRectangleArea(heights)
    print(res)
