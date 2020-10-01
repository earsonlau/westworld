# print("单调栈")

testcase1 = [1,2,3,4,5,6,7]
testcase2 = [7,6,5,4,3,2,1]
testcase3 = [3,1,6,4,2,7,5]

# 该函数的作用是打印每个元素左边离他最近的比他小的元素和右边离他最近的比他小的元素
# 时间复杂度O(N)

def monotonicstack1(list_):
    monotonicstack = []
    for i in range(len(list_)):
        if len(monotonicstack) == 0:
            # print("push第一个数")
            monotonicstack.append(i)
            continue
        elif list_[i-1] < list_[i]:
            # print("遇到比我大的，push一下")
            monotonicstack.append(i)
            continue
        else:
            # print("遇到比我小的，pop一下")
            res = monotonicstack.pop()
            left = (monotonicstack[0] if len(monotonicstack) != 0 else -1 )
            right = i
            monotonicstack.append(i)
            if left == -1 :
                print(list_[res],":","无",list_[right])
            else:
                print(list_[res],":",list_[left],list_[right])

    while len(monotonicstack) != 0 :
        res = monotonicstack.pop()
        left = monotonicstack[-1] if len(monotonicstack) != 0 else -1
        right = -1
        if left == -1 :
            print(list_[res], ":", "无", "无")
        else:
            print(list_[res], ":", list_[left], "无")

# monotonicstack(testcase2)


# 该函数的作用是打印每个元素左边离他最近的比他大的元素和右边离他最近的比他大的元素
# 时间复杂度O(N)

def monotonicstack2(list_):
    monotonicstack = []
    for i in range(len(list_)):
        if len(monotonicstack) == 0:
            # print("push第一个数")
            monotonicstack.append(i)
            continue
        elif list_[i-1] > list_[i]:
            # print("遇到比我小的，push一下")
            monotonicstack.append(i)
            continue
        else:
            # print("遇到比我大的，pop一下")
            res = monotonicstack.pop()
            left = (monotonicstack[0] if len(monotonicstack) != 0 else -1 )
            right = i
            monotonicstack.append(i)
            if left == -1 :
                print(list_[res],":","无",list_[right])
            else:
                print(list_[res],":",list_[left],list_[right])

    while len(monotonicstack) != 0 :
        res = monotonicstack.pop()
        left = monotonicstack[-1] if len(monotonicstack) != 0 else -1
        right = -1
        if left == -1 :
            print(list_[res], ":", "无", "无")
        else:
            print(list_[res], ":", list_[left], "无")

# monotonicstack2(testcase3)

#气温问题
# 给你一个数组 T = [73, 74, 75, 71, 69, 72, 76, 73]，这个数组存放的是近几天的天气气温
# （这气温是铁板烧？不是的，这里用的华氏度）。
# 你返回一个数组，计算：对于每一天，你还要至少等多少天才能等到一个更暖和的气温；如果等不到那一天，填 0 。
# 举例：给你 T = [73, 74, 75, 71, 69, 72, 76, 73]，你返回 [1, 1, 4, 2, 1, 1, 0, 0]。
# 解释：第一天 73 华氏度，第二天 74 华氏度，比 73 大，所以对于第一天，只要等一天就能等到一个更暖和的气温。后面的同理。


def dailyTemperatures(list_):
    monotonicstack = []
    result = [0] * len(list_)
    #从最后一个元素向第一个元素遍历
    for i in range(len(list_)-1,-1,-1):
        #如果单调栈栈顶元素比当前元素小，那么栈顶元素pop出来
        while len(monotonicstack)!= 0 and list_[monotonicstack[-1]] <= list_[i]:
            monotonicstack.pop()
        #如果此时单调栈内为空 说明第i个元素之后没有比他大的了 赋值为0
        #如果此时单调栈内非空 说明第i个元素之后有一个元素比他大 把索引之差赋值给result的i位置
        result[i] = 0 if len(monotonicstack) == 0 else monotonicstack[-1] - i
        monotonicstack.append(i)
    return result
print(dailyTemperatures(testcase2))