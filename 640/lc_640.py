class Solution:
    def solveEquation(self, equation):
        equation = equation.replace('-', '+-')
        left, right = equation.split('=')
        l_item = left.split('+')
        r_item = right.split('+')
        x_count = 0
        cons_value = 0
        for item in l_item:
            if item=='':
                continue
            if item.endswith('x'):
                pre = item[:-1]
                if pre == '':
                    x_count += 1
                elif pre == '-':
                    x_count -= 1
                else:
                    x_count += int(pre)
            else:
                cons_value -= int(item)

        for item in r_item:
            if item=='':
                continue
            if item.endswith('x'):
                pre = item[:-1]
                if pre == '':
                    x_count -= 1
                elif pre == '-':
                    x_count += 1
                else:
                    x_count -= int(pre)
            else:
                cons_value += int(item)

        if x_count == 0 and cons_value == 0:
            return "Infinite solutions"
        if x_count == 0 and cons_value != 0:
            return "No solution"

        res = cons_value / x_count
        return 'x=' + str(int(res))


if __name__ == '__main__':
    # equation = "x+5-3+x=6+x-2"
    # equation = "2x+3x-6x=x+2"
    equation = "-x=-1"
    solve = Solution()
    res = solve.solveEquation(equation)
    print(res)
