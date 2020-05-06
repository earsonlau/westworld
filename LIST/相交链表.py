# 编写一个程序，找到两个单链表相交的起始节点。
# 思路：若相交，链表A： a+c, 链表B : b+c. a+c+b+c = b+c+a+c 。则会在公共处c起点相遇。
# 若不相交，a +b + null = b+a +null 。因此相遇处是NULL。
#
#

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA