"""
思路：动态规划
我们令dp[i][j]是到达坐标点i,j的最多路径
动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
注意：对于第一行dp[0][j] 或者第一列dp[i][0] 由于都是在边界，所以只能为1
时间复杂度O(m*n)
空间复杂度O(m*n)
"""

import numpy as np
# class Solution:
#     def uniquePaths(self,m,n):
#         dp = np.zeros([m,n],np.int)
#         for i in range(n):#边界
#             dp[0][i] = 1
#         for i in range(n):#边界
#             dp[i][0] = 1
#         for i in range(m):
#             for j in range(n):#从上面来有多少条路+从左边来有多少条路 = 到这里有多少条路
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         return dp[m-1][n-1]
#
# a = Solution()
# print(a.uniquePaths(3,2))

#空间复杂度优化到O(2n)
import numpy as np
# class Solution:
#     def uniquePaths(self,m,n):
#         # dp = np.zeros([m,n],np.int)
#         pre = np.ones(n,np.int)
#         cur = np.ones(n,np.int)
#         # for i in range(n):#边界
#         #     dp[0][i] = 1
#         # for i in range(n):#边界
#         #     dp[i][0] = 1
#         for i in range(1,m):
#             for j in range(1,n):#从上面来有多少条路+从左边来有多少条路 = 到这里有多少条路
#                 cur[j] = cur[j-1] + pre[j]
#             pre = cur.copy()
#         return pre[n-1]
#
# a = Solution()
# print(a.uniquePaths(3,2))

#空间复杂度优化到O(n)
import numpy as np
class Solution:
    def uniquePaths(self,m,n):

        cur = np.ones(n,np.int)
        for i in range(1,m):
            for j in range(1,n):#从上面来有多少条路+从左边来有多少条路 = 到这里有多少条路
                cur[j] += cur[j-1]
        return cur[n-1]

a = Solution()
print(a.uniquePaths(3,2))
