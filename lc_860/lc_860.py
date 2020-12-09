class Solution:
    def lemonadeChange(self, bills):
        if not bills:
            return False
        bill_dir = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                bill_dir[bill] += 1
            elif bill == 10 and bill_dir[5] > 0:
                bill_dir[10] += 1
                bill_dir[5] -= 1
            elif bill == 20:
                if bill_dir[10] > 0 and bill_dir[5] > 0:
                    bill_dir[10] -= 1
                    bill_dir[5] -= 1
                elif bill_dir[5] > 2:
                    bill_dir[5] -= 3
                else:
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    solve = Solution()
    bills = [5, 5, 5, 10, 20]
    res = solve.lemonadeChange(bills)
    print(res)
