# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
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
# 说明：如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

# 递归，自顶向下（但是在递归到达base case的时候是自底向上走
#
# 思路:
# 用递归的方法做。边界条件是遍历到最下面一行。
# 要达到最下面一行，要么往下，要么往右下。
# 最短路径就是每次往下和往右下的元素选一个较小者。
# 而记忆化搜索就是把每次的结果做缓存.

def minimumTotal(triangle):
    row = len(triangle)  # 三角形的行数
    return process(0,0,row,triangle)
    # 参数一：第0行，参数二：第0行的索引0位置，参数三：总行数，参数四：三角形

def process(level, down, row, triangle):
    # level为可变参数，表示现在在第level行
    # down为可变参数，表示现在位于第down位
    # row为不变参数，表示这个三角形有多少行
    # triangle为不变参数，存放这个三角形
    if level == row - 1 :  # base case
        return triangle[level][down]  # 到最底了，没有往下走left和往右下走right了。
    # print("此时的level:",level,)
    # print("此时的c:",c)
    go_down = process(level+1, down, row, triangle)  # 往下走到(level+1,down)的距离记为go_down
    go_down_right = process(level+1, down+1, row, triangle)  # 往右下走到(level+1,down)的距离记为go_down_right
    # print("min(left,right): ",min(go_down,go_down_right) )
    # print("triangle","[",level,"][",down,"]):",triangle[level][down])
    # print("最短路径：",min(go_down,go_down_right) + triangle[level][down])
    return min(go_down,go_down_right) + triangle[level][down] # 返回本位置元素+接下来要走的最短一步



tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(tri))

# 自顶向下，记忆化搜索,走过的路直接存在memo里面，memo是一个三角形
#memo[i][j]代表输入的三角形的第i行第j个位置走到底部的最短路径
#
# memo = [[]]
def minimumTotal_withmemo(triangle):
    row = len(triangle)
    # memo是一个跟输入三角形形状一致的三角形数组
    # memo[i][j]存放的是三角形的[i][j]元素到底部的最短路径
    memo = [[0] * _ for _ in range(1,row+1)]
    return memoprocess(0, 0, row, memo, triangle)


def memoprocess(level, down, row, memo, triangle):
    # level为可变参数，表示现在在第level行
    # down为可变参数，表示现在位于第down位
    # row为不变参数，表示这个三角形有多少行
    # triangle为不变参数，存放这个三角形
    if memo[level][down] != 0:
        return memo[level][down]

    if level == row - 1 :  # base case
        memo[level][down] = triangle[level][down]  # 到最底了，没有往下走left和往右下走right了。
        return memo[level][down]

    go_down = memoprocess(level + 1, down, row, memo, triangle)  # 往下走到(level+1,down)的距离记为go_down
    go_down_right = memoprocess(level + 1, down + 1, row, memo, triangle)  # 往右下走到(level+1,down)的距离记为go_down_right

    memo[level][down] = min(go_down, go_down_right) + triangle[level][down] # 返回本位置元素+接下来要走的最短一步
    return memo[level][down]


tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal_withmemo(tri))
