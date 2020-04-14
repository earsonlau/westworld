# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:
#
# 输入:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]


#思路一:O(m+n)空间
#两遍扫矩阵，第一遍用集合记录有哪些行列有0，第二遍把该置零的置零
from typing import List
class Solution:
    def setZeros(self,matrix:List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix)
        row_zero = set()
        col_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)#存放0所在行的索引
                    col_zero.add(j)#存放0所在列的索引
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
        return matrix


#思路二:O(1)空间
class Solution:
    def setzeros(self,matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        #找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        #第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break
        #把第一行或第一列作为标志位
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        #置零
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0

        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0
        return matrix