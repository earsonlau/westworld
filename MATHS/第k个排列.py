# 给出集合 [1, 2, 3,…, n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3
# 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
# 给定 n
# 和 k，返回第 k 个排列。
#
# 说明：
#
# 给定
# n 的范围是[1, 9]。
# 给定
# k 的范围是[1,  n!]。
#
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
#
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"
#
# 解题思路：将
# n! 种排列分为：n
# 组，每组有(n - 1)!个排列，根据k值可以确定是第几组的第几个排列，选取该排列的第1个数字，然后递归从剩余的数字里面选取下一个数字，直到n = 1
# 为止。
#

class Solution:
    def getPermutation(self,n,k):
        visited = [False]*n
        # 将 n! 种排列分为：n 组，每组有 (n-1)! 种排列
        return self.recursive(n,self.factorial(n-1),k,visited)

    # n 剩余的数字个数，递减
    # f 每组的排列个数

    #     /**
    #     * @param n 剩余的数字个数，递减
    #     * @param f 每组的排列个数
    #     */
    def recursive(self,n,f,k,visited):
        offset = k % f # 组内偏移量
        groupIndex = k / f + (1 if offset > 0 else 0)
        # 在没有被访问的数字里找第 groupIndex 个数字
        for i in visited:
            if (not i) and (groupIndex > 0):
                groupIndex -= 1
        visited[i-1] = True
        if n-1 > 0:
            # offset = 0 时，则取第 i 组的第 f 个排列， 否则取第 i 组的第 offset 个排列
            return str(i) + self.recursive(n - 1,f / (n - 1) ,offset if offset == 0 else visited)
        else:
            # 最后一数字
            return str(i)

    def factorial(self,n):
        res = 1
        for i in range(n,1,-1):
            res *= i
        return res