import numpy as np
#
# 暴力搜索
#
def maximalRectangle(matrix):
    if (len(matrix) == 0):
        return 0
   # //保存以当前数字结尾的连续 1 的个数
    width = np.zeros([len(matrix),len(matrix[0])])
    maxArea = 0
    #//遍历每一行
    for row in range(len(matrix)):
        #遍历每一列
        for col in range(len(matrix[0])):
            #//更新 width
            if (matrix[row][col] == '1') :#看到1了！
                if (col == 0) :#矩阵的第一列
                    width[row][col] = 1
                else:
                    width[row][col] = width[row][col - 1] + 1
            else:#没看到1，置零
                width[row][col] = 0
            # //记录所有行中最小的数
            minWidth = width[row][col]
            # //向上扩展行
            for up_row in range(row,-1,-1):
                #计算高度height
                height = row - up_row + 1
                # //找最小的数作为矩阵的宽
                minWidth = min(minWidth, width[up_row][col])
                # //更新面积
                maxArea = max(maxArea, height * minWidth)
    return maxArea

rec = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(maximalRectangle(rec))


#
#
#