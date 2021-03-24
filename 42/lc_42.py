class Solution:
    def trap(self, height):
        if len(height)==0:
            return 0
        l = 0
        r = len(height) - 1
        lm = height[l]
        rm = height[r]
        res = 0
        while l < r:
            if height[l] > lm:
                lm = height[l]
            if height[r] > rm:
                rm = height[r]
            min_top = min(lm, rm)

            if height[l] < min_top:
                res += min_top - height[l]
            if height[r] < min_top:
                res += min_top - height[r]
            if lm < rm:
                l += 1
            else:
                r -= 1

        return res


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 0, 3, 2, 5]
    solve = Solution()
    res = solve.trap(height)
    print(res)
