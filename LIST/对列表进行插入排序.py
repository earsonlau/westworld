思路:
这个道题就像排队,先找个排头dummy,然后依次从head节点放入dummy,只需要依次dummy现有节点比较,插入其中!

1 	class Solution:
2 	    def insertionSortList(self, head: ListNode) -> ListNode:
3 	             # 找个排头
4 	        dummy = ListNode(-1)
5 	        pre = dummy
6 	        # 依次拿head节点
7 	        cur = head
8 	        while cur:
9 	                # 把下一次节点保持下来
10 	            tmp = cur.next
11 	            # 找到插入的位置
12 	            while pre.next and pre.next.val < cur.val:
13 	                pre = pre.next
14 	            # 进行插入操作
15 	            cur.next = pre.next
16 	            pre.next = cur
17 	            pre= dummy
18 	            cur = tmp
19 	        return dummy.next



因为我们每次都要从头比较,但是测试集很多都是顺序排列的,没必要从头开始,我们直接比较最后一个tail,放在后面!

1 	class Solution:
2 	    def insertionSortList(self, head: ListNode) -> ListNode:
3 	        # 找个排头
4 	        dummy = ListNode(float("-inf"))
5 	        pre = dummy
6 	        tail = dummy
7 	        # 依次拿head节点
8 	        cur = head
9 	        while cur:
10 	            if tail.val < cur.val:
11 	                tail.next = cur
12 	                tail = cur
13 	                cur = cur.next
14 	            else:
15 	                # 把下一次节点保持下来
16 	                tmp = cur.next
17 	                tail.next = tmp
18 	                # 找到插入的位置
19 	                while pre.next and pre.next.val < cur.val:
20 	                    pre = pre.next
21 	                # 进行插入操作
22 	                cur.next = pre.next
23 	                pre.next = cur
24 	                pre= dummy
25 	                cur = tmp
26 	        return dummy.next
