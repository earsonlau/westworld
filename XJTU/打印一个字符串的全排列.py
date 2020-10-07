#打印给定字符串的所有排列
class Code_04_Print_All_Permutations:
    def printAllPermutations1(self, str):
        chs = list(str)
        self.process1(chs, 0)
    # str[0...i-1]已经做好决定
    # str[i...]都有机会来到i位置
    def process1(self, chs, i):
        if i == len(chs):
            # i是终止位置，str当前的样子就是一种结果，打印
            print(chs)
        for j in range(i, len(chs)):
            # i不是终止位置，i之后的元素都可以来到i位置
            # j遍历i后面所有的字符
            chs[i], chs[j] = chs[j], chs[i]# 交换
            self.process1(chs, i + 1)#i+1之后的继续，i之前的不动
            chs[i], chs[j] = chs[j], chs[i]
            #恢复现场，回溯到最初始的状态，不然无法基于初始状态另外开一个新分支

sol = Code_04_Print_All_Permutations()
test1 = "aac"
sol.printAllPermutations1(test1)
print("======")

import numpy
class solution:
    def permutationNoRepeat(self,chs):
        res = []
        if len(chs) == 0:
            return res
        chs = list(chs)
        self.process2(chs,0,res)
        return res
#剪枝
    def process2(self,chs, i,res):
        if i == len(chs):
            # i是终止位置，str当前的样子就是一种结果，打印
            res.append(chs.copy())#靠 在一个list里面append(list2)会覆盖！！要拷贝一个副本后append才不会！
            return
        visited = numpy.zeros((26), dtype=bool) #定义一个bool类型的数组，减少重复计算
        for cur in range(i, len(chs)):
            # i不是终止位置，i之后的元素都可以来到i位置
            # j遍历i后面所有的字符
            if (not visited[ord(chs[cur])-ord('a')]):
                visited[ord(chs[cur])-ord('a')] = True
                chs[i], chs[cur] = chs[cur], chs[i]  # 交换
                self.process2(chs, i + 1, res)  # i+1之后的继续，i之前的不动
                chs[i], chs[cur] = chs[cur], chs[i]
                # 恢复现场，回溯到最初始的状态，不然无法基于初始状态另外开一个新分支
print(solution().permutationNoRepeat("aac"))
#靠！list append list 会覆盖！！