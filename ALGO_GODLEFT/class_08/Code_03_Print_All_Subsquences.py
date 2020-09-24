class Solution:
    #处理方式1：递归，起点是空字符串，每次决策是否要在结果加上str[i]
    def printAllSubString(self,str,i,res):
        if (i == len(str)):
            print(res)
            return
        else:
            self.printAllSubString(str,i+1,res)
            self.printAllSubString(str,i+1,res+str[i])

    #处理方式2：递归，起点是给定字符串，每次决策是否要舍去str[i]
    def process(self,chs,i):
        if (i == len(chs)):
            print(chs)
            return
        self.process(chs, i + 1)
        tmp = chs[i]
        chs = chs[:i]+' '+chs[i+1:]
        self.process(chs, i + 1)
        chs = chs[:i] + tmp + chs[i+1:]
# Solution().printAllSubString("abc",0,"")
# Solution().process("abc",0)