class Solution:
    # 这种解法是O(n)
    def getmin(self,stack):
        stackdata = stack
        stackmin = []
        while (len(stackdata) != 0):
            tmp = stackdata.pop()
            if(len(stackmin) == 0 or stackmin[-1]>=tmp):
                stackmin.append(tmp)
        return stackmin[-1]
# sol = Solution()
# stack= []
# stack.append(1)
# stack.append(2)
# stack.append(0)
# stack.append(5)
# print(sol.getmin(stack))


# O(1)的解法是，原stack push的时候stackmin也push，stackmin把最小值放在栈顶

class Stack(object):
    #初始化栈为空列表
    def __init__(self):
        self.stack = []
        self.__stackmin = []

    def isemptystack(self):
        return len(self.stack) == 0

    def isfullstack(self):
        return len(self.stack) == 10

    def push(self,e):
        if not self.isfullstack():
            self.stack.append(e)
            if len(self.__stackmin) == 0 or self.getmin() >= e:
                self.__stackmin.append(e)
            return 1

        return 0

    def pop(self):
        if self.isemptystack():
            return 0
        value = self.stack.pop()
        if value == self.getmin():
            self.__stackmin.pop()
        return self.stack.pop()

    def peek(self):
        if self.isemptystack():
            return 0
        return self.stack[len(self.stack)-1]

    def getmin(self):
        if len(self.__stackmin) == 0:
            print("your stack is empty.")
            return 0
        return self.__stackmin[-1]

s = Stack()
s.push(1)
s.push(5)
s.push(3)
s.push(1)
s.push(4)
print(s.getmin())