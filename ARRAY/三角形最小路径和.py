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

#递归，自顶向下（但是在递归到达base case的时候是自底向上走
#

def helper(level,c,row,triangle):
    if level == row -1 :#base case
        # print("到底了！打印一下第",level,"行第",c,"个元素")
        # print(triangle[level][c])
        return triangle[level][c]#到最底了
    # print("此时的level:",level,)
    # print("此时的c:",c)
    left = helper(level+1, c,row, triangle)#从左下方到(level,c)的距离
    right = helper(level+1, c+1, row, triangle)#从右下方到(level,c)的距离
    print("min(left,right): ",min(left,right) )
    print("triangle","[",level,"][",c,"]):",triangle[level][c])
    print("最短路径：",min(left,right) + triangle[level][c])
    # print("从左上方过来的距离:",left,"从右上方过来的距离:",right)
    return min(left,right) + triangle[level][c]

def minimumTotal(triangle):
    row = len(triangle)# 三角形的行数
    return helper(0,0,row,triangle)# 参数一：第0行，参数二：第0行的索引0位置，参数三：总行数，参数四：三角形

tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(tri))

# 自顶向下，记忆化搜索,走过的路直接存在memo里面，memo是一个三角形
#memo[i][j]代表输入的三角形的第i行第j个位置走到底部的最短路径
#
# memo = [[]]
def minimumTotal(triangle):
    row = len(triangle)
    # memo是一个跟输入三角形形状一致的三角形数组
    # memo[i][j]存放的是三角形的[i][j]元素到底部的最短路径
    memo = [[None] * _ for _ in range(1,row+1)]
    return helper(0, 0, row, memo, triangle)

def helper( level, c, row, memo, triangle):
    # print("helper: level=", level, " c=" , c)
    if (memo[level][c]!=None):
        return memo[level][c]
    if (level==row-1):
        memo[level][c] = triangle[level][c]
        return memo[level][c]
    left = helper(level+1, c, row, memo, triangle)#左下方到(level,c)的距离
    right = helper(level+1, c+1, row, memo, triangle)#右下方到(level,c)的距离
    memo[level][c] = min(left, right) + triangle[level][c]
    print("min(left,right): ",min(left,right) )
    print("triangle","[",level,"][",c,"]):",triangle[level][c])
    print("最短路径：",memo[level][c])
    # print(memo[level][c])
    print(memo)
    return memo[level][c]

tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(tri))

#自底向上

import numpy as np
def minimumTotal(triangle):#triangle是给定的三角形
    row = len(triangle)#计算三角形有多少行
    minlen = np.zeros(row+1)#初始化一个长度为row+1的数组，初始值为0
    for level in range(row-1,-1,-1):#从下往上遍历三角形的每一行
        for i in range(level+1):   #//第i行有level+1个数字，对第level行的每个索引i
            print("triangle[level][i]:",triangle[level][i])
            minlen[i] = min(minlen[i], minlen[i+1]) + triangle[level][i]#拿到最底的元素，往上走，按最短路径赋值给minlen[i]
            print("minlen",[i],":",minlen[i])
    return minlen[0]

tri = \
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(minimumTotal(tri))
