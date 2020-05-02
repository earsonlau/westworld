# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 非递归
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root: return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == sum_:
                res.append(tmp)
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res

# 递归


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        def helper(root, tmp, sum_):
            if not root:
                return
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)
        res = []
        helper(root, [], sum_)
        return res




