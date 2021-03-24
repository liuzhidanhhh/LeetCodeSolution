class Solution:
    def threeSum(self, nums):
        res = []
        nums = sorted(nums)
        for a_i, a_v in enumerate(nums):
            b = a_i + 1
            c = len(nums) - 1
            while b < c:
                if nums[b] + nums[c] == -a_v:
                    res.append((a_v, nums[b], nums[c]))
                    b += 1
                elif nums[b] + nums[c] < -a_v:
                    b += 1
                else:
                    c -= 1
        res = list(set(res))
        res = [list(r) for r in res]
        return res


if __name__ == '__main__':
    solve = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = solve.threeSum(nums)
    print(res)
