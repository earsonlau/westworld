# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
#  你可以对一个单词进行如下三种操作：
#
#  插入一个字符
#  删除一个字符
#  替换一个字符
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
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]# dp初始化为一个 m+1 x n+1 的矩阵
        #base case
        # base case 是 i 走完 s1 或 j 走完 s2，可以直接返回另一个字符串剩下的长度。
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        #自底向上求解
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    # 啥都别做（skip）
                    # i, j同时向前移动
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #三选一, 插入,删除,替换
                    dp[i][j] = min(dp[i-1][j] + 1, # 删除
                                   dp[i][j-1] + 1, # 插入
                                   dp[i-1][j-1] + 1 # 替换
                                   )
                    # # dp(i, j - 1) + 1, # 插入
                    # # 解释：
                    # # 我直接在 s1[i] 插入一个和 s2[j] 一样的字符
                    # # 那么 s2[j] 就被匹配了，前移 j，继续跟 i 对比
                    # # 别忘了操作数加一

                    # dp(i - 1, j) + 1,    # 删除
                    # # 解释：
                    # # 我直接把 s[i] 这个字符删掉
                    # # 前移 i，继续跟 j 对比
                    # # 操作数加一

                    # dp(i - 1, j - 1) + 1 # 替换
                    # # 解释：
                    # # 我直接把 s1[i] 替换成 s2[j]，这样它俩就匹配了
                    # # 同时前移 i，j 继续对比
                    # # 操作数加一

        #储存整个s1和s2的最小编辑距离
        return dp[m][n]

    def min(self,a,b,c):
        return min(a,min(b,c))

word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1,word2))