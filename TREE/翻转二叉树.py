# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

#递归
# class Solution {
#         public TreeNode invertTree(TreeNode root) {
#                 //递归函数的终止条件，节点为空时返回
#                 if(root==null) {
#                         return null;
#                 }
#                 //下面三句是将当前节点的左右子树交换
#                 TreeNode tmp = root.right;
#                 root.right = root.left;
#                 root.left = tmp;
#                 //递归交换当前节点的 左子树
#                 invertTree(root.left);
#                 //递归交换当前节点的 右子树
#                 invertTree(root.right);
#                 //函数返回时就表示当前这个节点，以及它的左右子树
#                 //都已经交换完了
#                 return root;
#         }
# }

class Solution:
    def invertTree(self,root):
        #递归函数的终止条件，节点为空时返回
        if root is None:
            return None
        #下面三句是将当前节点的左右子树交换
        tmp = root.right
        root.right = root.left
        root.left = tmp
        #递归交换当前节点的左子树
        self.invertTree(root.left)
        #递归交换当前节点的右子树
        self.invertTree(root.right)
        # 函数返回时就表示当前这个节点，以及它的左右子树
        # 都已经交换完了
        return root

#迭代

# 1
#
#
# class Solution {
# 2        public TreeNode invertTree(TreeNode root) {
# 3 if (root == null) {
# 4

# return null;
# 5 		}
# 6 			//将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
# 7 			LinkedL i st<TreeN ode> queue =
# new LinkedL i st<TreeN o de>();
# 8 			queue.add(root);
# 9 			wh ile(!queue.isEmpty()) {
# 10 				//每次都从队列中拿一个节点，并交换这个节点的左右子树
# 11 				TreeNode tmp = queue.poll();
# 12 				TreeNode left = tmp.left;
# 13 				tmp.left = tmp.right;
# 14 				tmp.right = left;
# 15 				//如果当前节点的左子树不为空，则放入队列等待后续处理
# 16 				if(tmp.l ef t!=null) {
# 17 					queue.add(tmp.left);
# 18 				}
# 19 				//如果当前节点的右子树不为空，则放入队列等待后续处理
# 20 				if(tmp.ri gh t!=null) {
# 21 					queue.add(tmp.right);
# 22 				}
# 23
# 24 			}
# 25 			//返回处理完的根节点
# 26 			return root;
# 27 		}28 	}

# 迭代
import queue
class Solution:
    def invertTree(self,root):
        if root is None:
            return None
        #将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        Q = queue.Queue()
        Q.put(root)
        while Q.not_empty():
            #每次都从队列中拿一个节点，并交换这个节点的左右子树
            tmp = Q.get()
            left = tmp.left
            tmp.left = tmp.right
            tmp.right = left
            # 如果当前节点的左子树不为空，则放入队列等待后续处理
            if tmp.left is not None:
                queue.put(tmp.left)
            # 如果当前节点的右子树不为空，则放入队列等待后续处理
            if tmp.right is not None:
                queue.put(tmp.right)
         # 返回处理完的根节点
        return root
