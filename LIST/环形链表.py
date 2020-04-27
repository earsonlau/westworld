# 给定一个链表，判断链表中是否有环。
#
# 用快慢指针

# boolean hasCycle(ListNode head) {
#     ListNode fast, slow;
#     fast = slow = head;
#     while (fast != null & & fast.next != null) {
#         fast = fast.next.next;
#         slow = slow.next;
#         if (fast == slow) return true;
#     }
#     return false;
# }