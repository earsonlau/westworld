# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#
# 递归
    1
    2 	public boolean hasPathSum(TreeNode root, int sum) {
    3 	    if (root == null) {
    4 	        return false;
    5 	    }
    6 	    return hasPathSumHelper(root, sum);
    7 	}
    8
    9 	private boolean hasPathSumHelper(TreeNode root, int sum) {
   10 	    //到达叶子节点
   11 	    if (root.left == null && root.right == null) {
   12 	        return root.val == sum;
   13 	    }
   14 	    //左孩子为 null
   15 	    if (root.left == null) {
   16 	        return hasPathSumHelper(root.right, sum - root.val);
   17 	    }
   18 	    //右孩子为 null
   19 	    if (root.right == null) {
   20 	        return hasPathSumHelper(root.left, sum - root.val);
   21 	    }
   22 	    return hasPathSumHelper(root.left, sum - root.val) || hasPathSumHelper(root.right, sum - root.val);
   23 	}


