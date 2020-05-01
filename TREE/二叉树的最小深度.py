# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.
#
# 另外这道题的关键是搞清楚递归结束条件
#
# 叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
# 当 root 节点左右孩子都为空时，返回 1
# 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
# 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值



   #  1 	class Solution {
   #  2 	    public int minDepth(TreeNode root) {
   #  3 	        if(root == null) return 0;
   #  4 	        //这道题递归条件里分为三种情况
   #  5 	        //1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
   #  6 	        if(root.left == null && root.right == null) return 1;
   #  7 	        //2.如果左孩子和由孩子其中一个为空，那么需要返回比较大的那个孩子的深度
   #  8 	        int m1 = minDepth(root.left);
   #  9 	        int m2 = minDepth(root.right);
   # 10 	        //这里其中一个节点为空，说明m1和m2有一个必然为0，所以可以返回m1 + m2 + 1;
   # 11 	        if(root.left == null || root.right == null) return m1 + m2 + 1;
   # 12
   # 13 	        //3.最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
   # 14 	        return Math.min(m1,m2) + 1;
   # 15 	    }
   # 16 	}


class Solution:
    def minDepth(self,root):
        if root is None: return 0
        #这道题递归条件里分为三种情况
        # 1. 左孩子和右孩子都为空的情况，说明到达了叶子节点，直接返回1即可
        if root.left is None and root.right is None:
            return 1
        #2. 如果左孩子和右孩子其中一个为空，那么需要返回比较大的那个孩子的深度
        m1 = self.minDepth(root.left)
        m2 = self.minDepth(root.right)
        # 这里其中一个节点为空，说明m1 和 m2 有一个必然为0， 所有可以返回 m1 + m2 + 1
        if (root.left is None or root.right is None):
            return m1 + m2 + 1
        #3. 最后一种情况，也就是左右孩子都不为空，返回最小深度 +1 即可
        return min(m1,m2) + 1





# 代码可以进行简化，当左右孩子为空时 m1m1 和 m2m2 都为 00
# 可以和情况 22 进行合并，即返回 m1+m2+1m1+m2+1
# 简化后代码如下:

   #  1 	class Solution {
   #  2 	    public int minDepth(TreeNode root) {
   #  3 	        if(root == null) return 0;
   #  4 	        int m1 = minDepth(root.left);
   #  5 	        int m2 = minDepth(root.right);
   #  6 	        //1.如果左孩子和右孩子有为空的情况，直接返回m1+m2+1
   #  7 	        //2.如果都不为空，返回较小深度+1
   #  8 	        return root.left == null || root.right == null ? m1 + m2 + 1 : Math.min(m1,m2) + 1;
   #  9 	    }
   # 10 	}
