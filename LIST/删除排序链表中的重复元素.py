# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#

# 思路：

#双指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self,head:ListNode):
        if (head is None or head.next is None):
            return head
        p = head # 慢指针
        q = head.next # 快指针
        while p.next is not None:
            if p.val == q.val: # 找到重复元素
                if q.next is None: # 快指针后面如果没有元素直接删除
                    p.next = None
                else:# 快指针后有元素
                    p.next = q.next
                    q = q.next
            else: #元素不相等
                p = p.next
                q = q.next
        return head

#直接法
class Solution:
    def deleteDuplicates(self,head: ListNode):
        if (head is not None or head.next):
            return head
        p = head
        while (p.next is not None and p is not None):
            if (p.val == p.next.val):
                p.next = p.next.next
            else:
                p = p.next
        return head

# 递归法
class Solution:
    def deleteDuplicates(self,head):
        if head is not None or head.next is not None:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            head = head.next
        return head

# 递归套路解决链表问题：
# 找终止条件：当head指向链表只剩一个元素的时候，自然是不可能重复的，因此return
# 想想应该返回什么值：应该返回的自然是已经去重的链表的头节点
# 每一步要做什么：宏观上考虑，此时head.next已经指向一个去重的链表了，
# 而根据第二步，我应该返回一个去重的链表的头节点。因此这一步应该做的是判断当前的head和head.next是否相等，
# 如果相等则说明重了，返回head.next，否则返回head。