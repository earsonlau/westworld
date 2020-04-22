import queue
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 在访问过程中，我们只需要将同一层中的节点同时入队列即可。在将该queue中所有元素出队列的同时，将下一层的元素进队列，完成交接

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self,root:TreeNode):
        res=[]
        if root is None:
	        return res
        Q = queue.Queue()
        Q.put(root)
        while(Q.empty()==False):
            a = []
            width=Q.qsize()
            for i in range(width):
                p = Q.get()
                a.append(p.val)
                if(p.left):Q.get(p.left)
                if(p.right):Q.get(p.right)
            res.append(a)
        return res
