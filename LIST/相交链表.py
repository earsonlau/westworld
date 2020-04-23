# 编写一个程序，找到两个单链表相交的起始节点。
# 思路：若相交，链表A： a+c, 链表B : b+c. a+c+b+c = b+c+a+c 。则会在公共处c起点相遇。若不相交，a +b = b+a 。因此相遇处是NULL。
#
#
#     1 	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
#     2 	    if (headA == null || headB == null) return null;
#     3 	    ListNode pA = headA, pB = headB;
#     4 	    while (pA != pB) {
#     5 	        pA = pA == null ? headB : pA.next;
#     6 	        pB = pB == null ? headA : pB.next;
#     7 	    }
#     8 	    return pA;
#     9 	}
