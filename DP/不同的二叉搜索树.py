# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
#  示例:
#
#  输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  Related Topics 树 动态规划


# 给定一个整数n,求以1 .. n 为节点组成的二叉搜索树有多少种？
# 1.写出所有以这个节点组成的所有二叉树，然后每棵二叉树判断是不是二叉搜索树。
# 2.动态规划
# 3.公式法
#
# 动态规划：
class Solution:
    def numTrees(self,n):
        dp = [0]* (n+1) # 对dp数组做初始化,全为0
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1): # i从2遍历到n
            for j in range(1,i+1):# j从1遍历到i
                dp[i] += dp[j-1] * dp[i-j]
                #解释:
                # 假设 n 个节点存在二叉排序树的个数是 G(n), 令 f(i) 为以 i 为根的二叉搜索树的个数, 则
                # G(n) = f(1) + f(2) + ... + f(n)
                # 当 i 为根节点时,其左子树节点个数为 i - 1 个,右子树节点个数为 n - i 个,则
                # f(i) = G(i - 1) * G(n - i)

        return dp[n]

#公式法
class Solution:
    def numTrees(self,n):
        c = 1
        for i in range(n):
            c = c * 2 (2 * i + 1) / (i + 2) # 卡特兰数
        return c
