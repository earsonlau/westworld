# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 拉链解法：
#
 	    # Node* connect(Node* root) {
 	    #     if (!root) return root;
 	    #     Node * left = root->left;
 	    #     Node * right = root->right;
 	    #     while(left) {
 	    #         left->next = right;
 	    #         left = left->right;
 	    #         right = right->left;
 	    #     }
 	    #     connect(root->left);
 	    #     connect(root->right);
  	    #     return root;
 	    # }


#迭代解法1
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if not root:
			return root
		queue = [root]
		while queue:
			size = len(queue)
			# 将队列中的元素串联起来
			tmp = queue[0]
			for i in range(1,size):
				tmp.next = queue[i]
				tmp = queue[i]
			# 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
			for _ in range(size):
				tmp = queue.pop(0)
				if tmp.left:
					queue.append(tmp.left)
				if tmp.right:
					queue.append(tmp.right)
		return root

# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/dong-hua-yan-shi-san-chong-shi-xian-116-tian-chong/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#迭代解法2
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if not root:
			return root
		pre = root
		# 循环条件是当前节点的left不为空，当只有根节点
		# 或所有叶子节点都出串联完后循环就退出了
		while pre.left:
			tmp = pre
			while tmp:
				# 将tmp的左右节点都串联起来
				# 注:外层循环已经判断了当前节点的left不为空
				tmp.left.next = tmp.right
				# 下一个不为空说明上一层已经帮我们完成串联了
				if tmp.next:
					tmp.right.next = tmp.next.left
				# 继续右边遍历
				tmp = tmp.next
			# 从下一层的最左边开始遍历
			pre = pre.left
		return root

# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/dong-hua-yan-shi-san-chong-shi-xian-116-tian-chong/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



#递归

class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		def dfs(root):
			if not root:
				return
			left = root.left
			right = root.right
			# 配合动画演示理解这段，以root为起点，将整个纵深这段串联起来
			while left:
				left.next = right
				left = left.right
				right = right.left
			# 递归的调用左右节点，完成同样的纵深串联
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return root

# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/dong-hua-yan-shi-san-chong-shi-xian-116-tian-chong/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
