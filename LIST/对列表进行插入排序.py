#  示例 1：
#
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
#  示例 2：
#
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#
#  Related Topics 排序 链表
# 思路:
# 这个道题就像排队,先找个排头dummy,然后依次从head节点放入dummy,只需要依次dummy现有节点比较,插入其中!
#


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 找个排头
        dummy = ListNode(-1)
        pre = dummy
        # 依次拿head节点
        cur = head
        while cur:
            # 把下一次节点保持下来
            tmp = cur.next
            # 找到插入的位置
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # 进行插入操作
            cur.next = pre.next
            pre.next = cur
            pre= dummy
            cur = tmp
        return dummy.next
#
#
#
# 因为我们每次都要从头比较,但是测试集很多都是顺序排列的,没必要从头开始,我们直接比较最后一个tail,放在后面!
#
# 1 	class Solution:
# 2 	    def insertionSortList(self, head: ListNode) -> ListNode:
# 3 	        # 找个排头
# 4 	        dummy = ListNode(float("-inf"))
# 5 	        pre = dummy
# 6 	        tail = dummy
# 7 	        # 依次拿head节点
# 8 	        cur = head
# 9 	        while cur:
# 10 	            if tail.val < cur.val:
# 11 	                tail.next = cur
# 12 	                tail = cur
# 13 	                cur = cur.next
# 14 	            else:
# 15 	                # 把下一次节点保持下来
# 16 	                tmp = cur.next
# 17 	                tail.next = tmp
# 18 	                # 找到插入的位置
# 19 	                while pre.next and pre.next.val < cur.val:
# 20 	                    pre = pre.next
# 21 	                # 进行插入操作
# 22 	                cur.next = pre.next
# 23 	                pre.next = cur
# 24 	                pre= dummy
# 25 	                cur = tmp
# 26 	        return dummy.next
