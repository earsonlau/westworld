class Queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity -1 # rear始终指向最后一个元素
        self.Q = [None] * capacity
        self.capacity = capacity

    def isfull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def Enqueue(self,e):
        # check if is full
        if self.isfull():
            print("Full")
            return 0
        #rear point to the ready position for e
        self.rear = (self.rear + 1) % self.capacity
        # put in the value
        self.Q[self.rear] = e
        # size increase
        self.size += 1
        # print
        print("successfully enqueue ", str(e))
        return 1

    def Dequeue(self):
        # check
        if self.isEmpty():
            print("empty")
            return 0
        # find
        res = self.Q[self.front]
        # front move
        self.front = (self.front + 1) % self.capacity
        # size decrease
        self.size -= 1
        print("Dequeue: ",res)
        return 1

if __name__ == '__main__':
    queue = Queue(30)
    queue.Enqueue(10)
    queue.Enqueue(20)
    queue.Dequeue()

