class Solution:
    def parseBoolExpr(self, expression):
        # fuhao = {'(', ')', '&', '|', '!', 't', 'f', ','}
        stack = []
        for s in expression:
            if s in ['&', '|', '!', 't', 'f']:
                stack.append(s)
            elif s == ')':
                exp_list = []
                op = ''
                while len(stack) > 0:
                    top = stack.pop()
                    if top in ['t', True]:
                        exp_list.append(True)
                    elif top in ['f', False]:
                        exp_list.append(False)
                    else:
                        op = top
                        break
                if op == '&':
                    stack.append(all(exp_list))
                elif op == '|':
                    stack.append(any(exp_list))
                else:
                    stack.append(not(exp_list[0]))

            else:
                continue

        return stack[0]


if __name__ == '__main__':
    # expression = "|(&(t,f,t),!(t))"
    expression = "!(f)"
    solve = Solution()
    res = solve.parseBoolExpr(expression)
    print(res)
