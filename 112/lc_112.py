# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
            else:
                return False
        elif root.left and root.right:
            return self.hasPathSum(root.left, targetSum - root.val) \
                   or self.hasPathSum(root.right, targetSum - root.val)
        elif root.left:
            return self.hasPathSum(root.left, targetSum - root.val)
        else:
            return self.hasPathSum(root.right, targetSum - root.val)



if __name__ == '__main__':
    # root = TreeNode(5,
    #                 TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
    #                 TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    root =TreeNode(-1, None, TreeNode(-1))
    targetSum = -2
    solve = Solution()
    res = solve.hasPathSum(root, targetSum)
    print(res)
