# 删除链表中等于给定值 val 的所有节点。
# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#
# 删除结点的步骤
#
# 找到该结点的前一个结点
# 进行删除操作
#
# 三种方法
#
# 删除头结点时另做考虑（由于头结点没有前一个结点）
# 添加一个虚拟头结点，删除头结点就不用另做考虑
# 递归
#
# 方法一（删除头结点时另做考虑）
# 1
#
#
# class Solution {
# 2        public ListNode removeElements(ListNode head, int val) {
# 3 // 删除值相同的头结点后，可能新的头结点也值相等，用循环解决
# 4
#
#
# while (head != null & & head.val == val){
# 5                head=head.next;
# 6 	}
# 7 	 if(head==null ) 8 	            return
# head;
# 9 	        Li
# tNod e prev=head;
# 10 	        //确保当前结点后还有结点
# 11 	        while(pre v. next!=null){
# 12 	            if(prev.ne xt .val==val){
# 13 	                prev.next=prev.next.next;
# 14 	            }else{
# 15 	                prev=prev.next;
# 16 	            }
# 17 	        }
# 18 	        return head;
# 19 	}
# 20 	}
#
# 方法二（添加一个虚拟头结点）
# 1 	class Solution {
# 2 	    public ListNode removeElements(ListNode head, int val) {
# 3 	        //创建一个虚拟头结点
# 4 	        ListNode dummyNode=new ListNode(val-1);
# 5 	        dummyNode.next=head;
# 6 	        ListNode prev=dummyNode;
# 7 	        //确保当前结点后还有结点
# 8 	        w hile(prev. ne xt!=null){
# 9 	            if(prev.next .v al==val){
# 10 	                prev.next=prev.next.next;
# 11 	            } else{
# 12 	                prev=prev.next;
# 13 	            }
# 14 	        }
# 15 	        return dummyNode.next;
# 16 	    }17 	}
#
# 方法三（递归）
#
# 1 	class Solution {
# 2 	    public ListNode removeElements(ListNode head, int val) {
# 3 	       if (h ead==null)
# 4 	           return null;
# 5 	        head . next=removeElements(head. next,val);
# 6 	        if(hea d. val=
# =val){
#     7 	            return head.next;
# 8 	 }else{
# 9
# return head;
# 10 	        }
# 11 	    }
# 12 	}
#
#
#
