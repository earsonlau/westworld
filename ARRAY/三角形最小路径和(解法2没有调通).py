# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

#递归，自顶向下（这个递归打了log还是没看明白是怎么回事？？？
#
# def helper(level,c,row,triangle):
#     print("row:",row)
#     if level == row -1 :
#         print("到底了！输出第",level+1,"行第",c+1,"个元素")
#         print(triangle[level][c])
#         return triangle[level][c]#到最底了
#     print("level:",level,)
#     print("c:",c)
#     left = helper(level+1, c,row, triangle)#从左上方过来的距离
#     right = helper(level+1, c+1, row, triangle)#从右上方过来的距离
#     print("从左上方过来的距离:",left,"从右上方过来的距离:",right)
#     return min(left,right) + triangle[level][c]
#
# def minimumTotal(triangle):
#     row = len(triangle)
#     return helper(0,0,row,triangle)
#
# tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
# print(minimumTotal(tri))

#自顶向下，记忆化搜索

# memo = [[]]
# 没有看懂
# def minimumTotal(triangle):
#     row = len(triangle)
#     memo = [[None]*row]*row
#     return helper(0, 0, row, memo, triangle)
#
# def helper( level, c, row, memo, triangle):
#     print("helper: level=", level, " c=" , c)
#     if (memo[level][c]!=None):
#         return memo[level][c]
#     if (level==row-1):
#         memo[level][c] = triangle[level][c]
#         return memo[level][c]
#     left = helper(level+1, c, row, memo, triangle)
#     right = helper(level+1, c+1, row, memo, triangle)
#     memo[level][c] = min(left, right) + triangle[level][c]
#     print(memo[level][c])
#     return memo[level][c]
#
# tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
# print(minimumTotal(tri))


#
# import numpy as np
# #自底向上
# def minimumTotal(triangle):
#     row = len(triangle)
#     minlen = np.zeros(row+1)
#     for level in range(row-1,-1,-1):
#         for i in range(level+1):   #//第i行有i+1个数字
#             minlen[i] = min(minlen[i], minlen[i+1]) + triangle[level][i]
#     return minlen[0]