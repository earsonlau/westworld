# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false
import numpy as np
class Solution:
    def isMatch(self,s, p):
        sLen = len(s)
        pLen = len(p)
        # //dp[i][j]表示s1的前i个字符，和s2的前j个字符，能否匹配
        dp1 = [[False]*(pLen+1)]*(sLen+1)#不能使用dp1，修改dp[0][0]会把所有行的第一个元素都修改
        dp = [[False] * (pLen+1) for _ in range(sLen+1)] # 使用dp，修改dp[0][0]只修改第一行第一列的元素
        print(dp1)
        print(dp)

        # vector<vector<bool>>dp(sLen + 1, vector<bool>(pLen + 1, false));
        # //初始化 base situation：
        # //1. 初始原点 "" 和 "" 是匹配的
        dp[0][0] = True
        # //2. 初始化第一列：对于s1为"",s2只有1个或者多个*才可以匹配才可以匹配
        for i in range(1,pLen + 1):
            # (int i = 1; i <= pLen; i++) { //注意下标范围 pLen也要取
            # //注意p的下标变化
            if(dp[0][i - 1] and (p[i - 1] == '*')):
                dp[0][i] = True
        # //3. 对于第一行，已经初始化为false了
        # // 动态规划
        for i in range(1,sLen+1):
            for j in range(1,pLen +1):
                if(s[i - 1] == p[j - 1] or p[j - 1] == '?'):
                    print("i:",i,"j:",j)
                    dp[i][j] = dp[i - 1][j - 1] #//当前匹配，结果看前面是否匹配
                # // 两种情况不可能同时存在，这里写出else if也是可以的
                elif(p[j - 1] == '*'):
                    #// 匹配0个 ==>  dp[i][j-1]
                    #// 匹配1个：这里不是dp[i-1][j-1]，因为动态规划管好自己就好了，不能因为自己匹配了，就不让前面的串和*匹配 ==> dp[i - 1][j]
                    dp[i][j] = (dp[i][j - 1] or dp[i - 1][j])
        return dp[sLen][pLen]
s = "bb"
p = "b"
print(Solution().isMatch(s,p))