# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
#  你可以对一个单词进行如下三种操作：
#
#
#  插入一个字符
#  删除一个字符
#  替换一个字符
#
#
#
#
#  示例 1：
#
#  输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
#  示例 2：
#
#  输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#  Related Topics 字符串 动态规划


class Solution:
    def minDistance(self,s1,s2):
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        #base case
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        #自底向上求解
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1,dp[i][j-1] + 1,dp[i-1][j-1] + 1)
        #储存整个s1和s2的最小编辑距离
        return dp[m][n]

    def min(self,a,b,c):
        return min(a,min(b,c))

word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1,word2))