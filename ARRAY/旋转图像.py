# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:
#
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
from typing import List

# 思路1：


# class Solution:
#     def rotate(self,matrix:List[List[int]]) -> None:
#         """
#         Do not return anything,modify matrix in-place instead
#         """
#         n = len(matrix)
#         for i in range(n // 2):
#             for j in range(i,n-i-1):
#                 print("i:",i,",j:",j)
#                 print("matrix[i][j]",matrix[i][j])
#                 print("matrix",matrix)
#                 # 不能把这个长代码拆成四个语句，因为拆成四个语句每个语句都会面对不同的matrix。
#                 # 但是一个长语句会一直面对同一个matrix。
#                 matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = \
#                     matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]
#         print(matrix)
#
# a = Solution()
# matrix = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
# a.rotate(matrix)

#思路2：




class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = matrix[::-1] #翻转整个数组
        print(matrix)
        for i in range(0, n):
            for j in range(i+1, n):
                #print(i, j)
	                      #按正对角线交换两边的数
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

a = Solution()
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
a.rotate(matrix)