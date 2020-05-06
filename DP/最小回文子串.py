# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#  示例 2：
#
#  输入: "cbbd"
# 输出: "bb"
#
#  Related Topics 字符串 动态规划
#
# key：双指针
#
# 寻找回文串的问题核心思想是：从中间开始向两边扩散来判断回文串。
#
class Solution:
    def palindrome_check(self,s,l,r): # l向左走, r向右走, 找到最长的对称串
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    def palindrome(self, s): # 
        if len(s) < 2 :
            return s
        res = s[0]
        for i in range(len(s)):
            # 以s[i]为中心的文本串
            s1 = self.palindrome_check(s, i, i)
            # 以 s[i]和 s[i+1]为中心的回文串
            s2 = self.palindrome_check(s,i,i+1)
            # res = longest(res,s1,s2)
            res = res if(len(res) > len(s1)) else s1
            res = res if(len(res) > len(s2)) else s2
        return res

ss = "cbbbbbbbbbbbd"
print(Solution().palindrome(ss))


