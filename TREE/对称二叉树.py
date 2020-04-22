# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 思路
# 递归结束条件：
#
# 	都为空指针则返回 true
# 	只有一个为空则返回 false
# 递归过程：
#
# 	判断两个指针当前节点值是否相等
# 	判断 A 的右子树与 B 的左子树是否对称
# 	判断 A 的左子树与 B 的右子树是否对称
# 短路：
#
# 在递归判断过程中存在短路现象，也就是做 与 操作时，如果前面的值返回 false 则后面的不再进行计算

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isMirror(self,t1: TreeNode ,t2: TreeNode):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)



    def isSymmetric(self,root:TreeNode):
        return self.isMirror(root,root)


