# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 示例:
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
#
# 思路：
# 	生成一个 n×n 空矩阵 mat，随后模拟整个向内环绕的填入过程：
# 		定义当前左右上下边界 l,r,t,b，初始值 num = 1，迭代终止值 tar = n * n；
# 		当 num <= tar 时，始终按照 从左到右 从上到下 从右到左 从下到上 填入顺序循环，每次填入后：
# 			执行 num += 1：得到下一个需要填入的数字；
# 			更新边界：例如从左到右填完后，上边界 t += 1，相当于上边界向内缩 1。
# 		使用num <= tar而不是l < r || t < b作为迭代条件，是为了解决当n为奇数时，矩阵中心数字无法在迭代过程中被填充的问题。
# 最终返回 mat 即可。
import numpy as np
class Solution:
    def generateMatrix(self,n):
        l = 0 # 左边界
        r = n - 1 # 右边界
        t = 0 # 上边界
        b = n - 1 # 下边界
        mat = np.zeros([n,n]) # 生成一个 n x n 的零矩阵
        num = 1 # 迭代初始值
        tar = n * n # 迭代终止值
        while num <= tar: # 每次填一个数
            for i in range(l,r+1):
                mat[t][i] =  num # 从左到右填数 (left to right.
                num += 1 # 填的是递增的数
            t += 1 # 上边界往下夹
            for i in range(t, b + 1):
                mat[i][r] = num # 从上到下填数 (top to bottom.
                num += 1 # 填的是递增的数
            r -= 1 #右边界往左夹
            for i in range(r, l - 1,-1):
                mat[b][i] = num # 从右到左填数 (right to left.
                num += 1
            b -= 1 # 下边界往上夹
            for i in range(b,t-1,-1):
                mat[i][l] = num # 从下往上填数 (bottom to top.
                num += 1
            l += 1 #左边界往右夹
        return mat

a = Solution()
print(a.generateMatrix(n = 3))