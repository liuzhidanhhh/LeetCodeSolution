# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ls = []

    # 中序遍历得到递增数组
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.ls.append(node.val)
            self.inorder(node.right)

    def findMode(self, root):
        # 异常情况判断
        if not root:
            return []
        self.inorder(root)

        # 统计每个数出现的次数，用字典存储
        value_count = {}
        for v in self.ls:
            if v not in value_count:
                value_count[v] = 1
            else:
                value_count[v] += 1

        # 字典按值排序，得到递减序
        count = sorted(value_count.items(), key=lambda kv: kv[1], reverse=True)

        # 统计所有众数
        res = []
        max_value = count[0][1]
        res.append(count[0][0])
        for item in count[1:]:
            if item[1] == max_value:
                res.append(item[0])
            else:
                break
        return res


# 不存储中序遍历数据
class Solution1:
    def __init__(self):
        self.value = None
        self.count = 0
        self.max_count = 0
        self.result = []

    def update(self, new_value):
        if new_value != self.value:
            self.value = new_value
            self.count = 1
        else:
            self.count += 1
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [new_value]
        elif self.count == self.max_count:
            self.result.append(new_value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.update(node.val)
            self.inorder(node.right)

    def findMode(self, root):
        if not root:
            return self.result
        self.inorder(root)
        return self.result


# Morris算法中序遍历BST
class Solution_Morris:
    def __init__(self):
        self.value = None
        self.count = 0
        self.max_count = 0
        self.result = []

    def update(self, value):
        if value != self.value:
            self.value = value
            self.count = 1
        else:
            self.count += 1
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [value]
        elif self.count == self.max_count:
            self.result.append(value)

    def findMode(self, root):
        if not root:
            return self.result

        cur = root
        while cur:
            if not cur.left:
                self.update(cur.val)
                cur = cur.right
            else:
                most_right = cur.left
                while most_right.right:
                    most_right = most_right.right

                most_right.right = cur
                pre = cur.left
                cur.left = None
                cur = pre
        return self.result


if __name__ == '__main__':
    a = Solution_Morris()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    res = a.findMode(root)
    print(res)
