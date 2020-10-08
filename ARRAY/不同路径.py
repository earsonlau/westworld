# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
# 示例 1:
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:
#
# 输入: m = 7, n = 3
# 输出: 28

"""
思路：
我们令dp[i][j]是到达坐标点i,j的最多路径
而到i,j的路径数就是到(i,j)上方一格 -> (i-1,j)的路径数+ 到(i,j)左方一格的路径数
动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1](要到(i,j)，要么从(i-1,j)往下走一格,要么从(i,j-1)往右走一格
注意：对于第一行dp[0][j] 或者第一列dp[i][0] 由于都是在边界，所以只能为1
时间复杂度O(m*n)
空间复杂度O(m*n)
"""

import numpy as np
class Solution:
    def uniquePaths(self,m,n):
        dp = np.zeros([m,n],np.int)
        for i in range(n):#边界
            dp[0][i] = 1
        for i in range(n):#边界
            dp[i][0] = 1
        for i in range(m):
            for j in range(n):#从上面来有多少条路+从左边来有多少条路 = 到这里有多少条路
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

a = Solution()
print(a.uniquePaths(3,2))


# 优化一：将一个表优化成了表中我们需要的两行
#空间复杂度优化到O(2n)
import numpy as np
class Solution:
    def uniquePaths(self,m,n):
        pre = np.ones(n,np.int)# pre为长度n初始值均为1的数组
        cur = np.ones(n,np.int)# cur为长度n初始值均为1的数组
        for i in range(1,m):
            for j in range(1,n):
                #cur[j-1]是从左边来的,pre[j]是从上面来的
                cur[j] = cur[j-1] + pre[j]
            pre = cur.copy()
        return pre[n-1]

a = Solution()
print(a.uniquePaths(3,2))

# 优化二：在优化一的基础上，将两行优化成了我们需要的当前行，因为cur未更新前保存的结果是上一行的结果
# #空间复杂度优化到O(n)
import numpy as np
class Solution:
    def uniquePaths(self,m,n):
        cur = np.ones(n,np.int)
        for i in range(1,m):
            for j in range(1,n):
                  # 等号右边的cur[j]是上一行的第j个数据对应的步数,cur[j-1]是本行第j-1个数据对应的步数
                # 等号右边的cur[j]是从上面来,等号右边的cur[j-1]是从左边来
                cur[j] = cur[j] + cur[j-1]
        return cur[n-1]

a = Solution()
print(a.uniquePaths(3,2))
