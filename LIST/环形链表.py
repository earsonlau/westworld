# 给定一个链表，判断链表中是否有环。
# 思路：


# 用快慢指针
class Solution:
    def hasCycle(self,head):
        fast = head
        slow = head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

