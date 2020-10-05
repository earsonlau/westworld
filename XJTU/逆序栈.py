#栈的反转
class Code_06_ReverseStackUsingRecursive :
    def reverse(self,stack):
        if (len(stack) == 0):
            return
        i = self.getAndRemoveLastElement(stack)
        self.reverse(stack)
        stack.append(i)

    def getAndRemoveLastElement(self,stack):
        result = stack.pop()
        if len(stack)==0:
            return result
        else:
            last = self.getAndRemoveLastElement(stack)
            stack.append(result)
            return last
sol = Code_06_ReverseStackUsingRecursive()
test = []
test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
sol.reverse(test)
while not len(test) == 0:
    print(test.pop())