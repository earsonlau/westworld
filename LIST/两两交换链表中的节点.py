# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
# 思路:

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        thead = ListNode(-1)
        thead.next = head
        c = thead # c指向头结点
        while c.next and c.next.next:# 第1个位置和第二个位置
            a, b=c.next, c.next.next# a是前面那个位置的节点，b是后面那个位置的节点
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next
