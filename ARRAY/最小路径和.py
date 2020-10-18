# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

# 思路:
# 动态规划
# 画一张二维表dp，dp(i,j)表示走到(i,j)位置的最小路径和
# 因为只能从上面来或者从左边来，这两个方向挑一个路径和最小的（边界特殊处理）

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]#从第一行往右走的状态转移方程(因为没有grid[i-1])
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]#从第一列往下走状态转移方程(因为没有grid[j-1])
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]#不在第一行也不在第一列的情况
        return grid[-1][-1]