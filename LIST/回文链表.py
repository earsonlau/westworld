# 请判断一个链表是否为回文链表。
# 示例 1:
# 输入: 1->2
# 输出: false
# 示例 2:
# 输入: 1->2->2->1
# 输出: true
#
# 思路：
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome (head:ListNode):
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        pre = head
        prepre = None
        while( fast is not None and fast.next is not None):
            pre = slow
            slow = slow.next
            fast = fast.next.next
            pre.next = prepre
            prepre = pre

        if fast is not None:
            slow = slow.next

        while pre is not None and slow is not None:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next

        return True
