# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6
from typing import List
# 方法一
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        row = len(matrix)
        col = len(matrix[0])
        height = [0] * (col + 2)
        res = 0
        for i in range(row):
            stack = []
            for j in range(col + 2):
                if 1<=j<=col:
                    if matrix[i][j-1] == "1":
                        height[j] += 1
                    else:
                        height[j] = 0
                while stack and height[stack[-1]] > height[j]:
                    cur = stack.pop()
                    res = max(res, (j - stack[-1] - 1)* height[cur])
                stack.append(j)
        return res

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/maximal-rectangle/solution/yu-zhao-zui-da-ju-xing-na-ti-yi-yang-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 动态规划
# 用height_j记录第i行为底,第j列高度是多少.
#
# 用left_j记录第i行为底, 第j列左边第一个小于height_j[j]的位置
#
# 用right_j记录第i行为底, 第j列右边第一个小于height_j[j]的位置

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        row = len(matrix)
        col = len(matrix[0])
        left_j = [-1] * col
        right_j = [col] * col
        height_j = [0] * col
        res = 0
        for i in range(row):
            cur_left = -1
            cur_right = col

            for j in range(col):
                if matrix[i][j] == "1":
                    height_j[j] += 1
                else:
                    height_j[j] = 0

            for j in range(col):
                if matrix[i][j] == "1":
                    left_j[j] = max(left_j[j], cur_left)
                else:
                    left_j[j] = -1
                    cur_left = j

            for j in range(col - 1, -1, -1):
                if matrix[i][j] == "1":
                    right_j[j] = min(right_j[j], cur_right)
                else:
                    right_j[j] = col
                    cur_right = j
            for j in range(col):
                res = max(res, (right_j[j] - left_j[j] - 1) * height_j[j])
        return res

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/maximal-rectangle/solution/yu-zhao-zui-da-ju-xing-na-ti-yi-yang-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

