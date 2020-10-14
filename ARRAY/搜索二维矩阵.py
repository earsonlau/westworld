# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 示例 2:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false

#这波啊，这波是二分查找！

# 思路:


class Solution:
    def searchMatrix(self,matrix,target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        #二分查找
        left,right = 0, m * n -1#直接把矩阵拍成一条,从前到后二分查找
        while (left <= right):
            pivot_idx = (left+right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n ]#利用了矩阵的特性
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3

print(Solution().searchMatrix(matrix,target))