# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划



class Solution:
    def climbStairs(self, n: int) -> int:
        """
        爬到第n楼的方法，为爬到第n-1楼和n-2楼的方法之和
        因为爬到n-1楼后，再爬1楼就能到达n楼
        爬到n-2楼同理
        因此只需初始化爬到1楼和爬到2楼分别有多少种方法，便可以推导出爬到n楼的方法
        """
        first = 1  # 爬到1楼只有1种方法
        second = 2  # 爬到2楼有两种方法
        res = 0  # 初始化爬到n楼的方法
        for i in range(3, n+1):  # 从3楼开始算
            res = first + second
            first = second  # 推导下一层  # 爬到 n - 2 楼的方法数赋值给first
            second = res # 爬到 n - 1 楼的方法数赋值给second
        return max(n, res)  # 返回n和res中较大的那个
print(Solution().climbStairs(4))

