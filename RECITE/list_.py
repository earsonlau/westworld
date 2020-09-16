# basic operations of linked list.

class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def headpush(self,x):
        new_node = ListNode(x)
        new_node.next = self.head
        self.head = new_node

    def tailpush(self,x):
        new_node = ListNode(x)
        temp=self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        temp = self.head
        while(temp.next.next is not None):
            print("push ",temp.next.data)
            self.headpush(temp.next.data)
            temp.next = temp.next.next
        print("push last one", temp.next.data)
        self.headpush(temp.next.data)
        temp.next = None

    def delete_node_first(self,x):
        #delete first node who's data is x
        temp = self.head
        while(temp.next.data != x):
            temp = temp.next
        temp.next = temp.next.next

    def delete_node_all(self,x):
        #delete all nodes whose data is x
        while(self.head is not None and self.head.data == x):
            self.head = self.head.next

        if self.head.next is None:
            return self.head
        prev = self.head

        while(prev.next is not None):
            print("next data is:",prev.next.data)

            if prev.next.data == x:
                prev.next = prev.next.next
                print("it is deleted!")
            else:
                prev = prev.next
            print("next one!")
        return self.head

    def search(self,x):
        index = 0
        temp = self.head
        while (temp.data!=x):
            temp = temp.next
            index+=1
        print(index)

    def removeNthFromEnd(self,n):
        p = self.head
        q = self.head
        for i in range (n+1):
            q = q.next
        while q:
            p = p.next
            q = q.next
        delnode = p.next
        print("remove:",delnode.data)
        p.next = p.next.next
        return self

    def drop_duplicate(self):
        p = self.head
        q = self.head.next
        while p.next is not None:
            if p.data == q.data:
                if q.next is  None:
                    p.next  = None
                else:
                    p.next = q.next
                    q = q.next
            else:
                p = p.next
                q = q.next
        return self.head

class Soluion:
    def merge_two_list(self,l1,l2):
        if not l1: return l2
        if not l2: return l1
        if l1.data <= l2.data:
            l1.next = self.merge_two_list(l1.next,l2)
            return l1
        else:
            l2.next = self.merge_two_list(l1,l2.next)
            return l2

if __name__ == '__main__':
    #create a linked list
    llist = LinkedList()
    llist.head = ListNode(1)
    llist.tailpush(2)
    llist.tailpush(3)
    llist.tailpush(3)
    llist.tailpush(3)
    # llist.printList()
    # print("now delete all the 4:")
    # llist.delete_node_all(4)
    llist.printList()
    llist.drop_duplicate()
    llist.printList()
    # print("now reverse")
    # llist.reverse()
    # llist.printList()
    # llist.removeNthFromEnd(2)
    # llist.printList()
    # l1 = LinkedList()
    # l2 = LinkedList()
    # l1.headpush(3)
    # l1.headpush(2)
    # l1.headpush(1)
    # l2.headpush(6)
    # l2.headpush(5)
    # l2.headpush(4)
    # l3 = Soluion().merge_two_list(l1.head,l2.head)
    # while(l3):
    #     print(l3.data)
    #     l3=l3.next
