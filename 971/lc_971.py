import copy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage):
        self.i = 0
        self.res = []

        def dfs(node):
            if not node:
                return
            if node.val != voyage[self.i]:
                self.res = [-1]
                return
            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                self.res.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        if -1 in self.res:
            self.res = [-1]
        return self.res


if __name__ == '__main__':
    solve = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    voyage = [1, 2, 5, 4, 3]
    res = solve.flipMatchVoyage(root, voyage)
    print(res)
