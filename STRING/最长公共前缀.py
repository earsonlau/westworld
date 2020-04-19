# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
# 思路：
# 思路 1：
# Python 特性，取每一个单词的同一位置的字母，看是否相同。
#
# 思路 2：
# 取一个单词 s，和后面单词比较，看 s 与每个单词相同的最长前缀是多少！遍历所有单词
#
# 思路 3：
# 按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。
#
#
# 代码:
# 思路一：
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs): #对strs进行解压，各取第一位丢进变量tmp
            print("tmp:",tmp)
            tmp_set = set(tmp)#把tmp中的几个字符丢进一个set里面。也就是去重。
            if len(tmp_set) == 1:#去重后长度为1，表示是公共字符
                res += tmp[0]
            else:
                break
        return res

# a =  ["flower","flow","flight"]
# print(Solution().longestCommonPrefix(a))
# 思路二：使用find方法
#
#Return the lowest index in s where the substring sub is found such that sub
# is wholly contained in s[start:end]. Return -1 on failure.
# Defaults for start and end and interpretation of negative values is the same as for slices.
from typing import List
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0] #第一个单词
        print(res)
        i = 1
        while i < len(s): #后面的单词
            print("i:",i)
            print("s[i]:",s[i])
            print("common:",s[i].find(res))
            while s[i].find(res) != 0:
                print("res[0:len(res)-1]:",res[0:len(res)-1])
                res = res[0:len(res)-1]#res是一直变化的。每次都拿res和s[i]做比对。
            i += 1
        return res

a =  ["flower","flow","flight"]
print(Solution().longestCommonPrefix(a))
#
# 思路三:
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()#按字典序排序
        n = len(s)
        a = s[0]
        b = s[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res
