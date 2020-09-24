#打印给定字符串的所有排列
class Code_04_Print_All_Permutations:
    def printAllPermutations1(self, str):
        chs = list(str)
        self.process1(chs, 0)

    def process1(self, chs, i):
        if i == len(chs):
            print(chs)
        for j in range(i, len(chs)):
            chs[i], chs[j] = chs[j], chs[i]
            self.process1(chs, i + 1)
            chs[i], chs[j] = chs[j], chs[i]

sol = Code_04_Print_All_Permutations()
test1 = "abcde"
sol.printAllPermutations1(test1)
print("======")

