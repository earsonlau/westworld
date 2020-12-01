# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划

#
#
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         """
#         爬到第n楼的方法，为爬到第n-1楼和n-2楼的方法之和
#         因为爬到n-1楼后，再爬1楼就能到达n楼
#         爬到n-2楼同理
#         因此只需初始化爬到1楼和爬到2楼分别有多少种方法，便可以推导出爬到n楼的方法
#         """
#         first = 1  # 爬到1楼只有1种方法
#         second = 2  # 爬到2楼有两种方法
#         res = 0  # 初始化爬到n楼的方法
#         for i in range(3, n+1):  # 从3楼开始算
#             res = first + second
#             first = second  # 推导下一层  # 爬到 n - 2 楼的方法数赋值给first
#             second = res # 爬到 n - 1 楼的方法数赋值给second
#         return max(n, res)  # 返回n和res中较大的那个
# print(Solution().climbStairs(4))



# 爬楼梯问题
# 版本一：一次迈一步或两步
def climbstair1(N):
    dp = [None]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
       dp[i] = dp[i-1]+dp[i-2]
    return dp[N]
# print(climbstair1(3))
# 版本二：一次迈1~k步
def climbstair2(N,k):
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        for j in range(1,k):
            if i < k:
                continue
            dp[i] += dp[i-k]
    return dp[N]
# print(climbstair2(3,2))
# 版本三：一次迈1~k步，有的台阶不能踩
def climbstair3(N,k,stairs):
    dp = [None]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        for k in range(1,k):
            if i < k :
                continue
            if stairs[i-1] == False:
                dp[i] = 0
            dp[i] += dp[i-k]
    return dp[N]
# print(climbstair3(3,2,[False,True,True]))
# 版本四：一次迈1~2步，每个台阶有一个cost，最小化总的cost
def climbstair4(N,p):
    dp = [None]*(N+1)
    dp[0] = 1
    dp[1] = p[1]
    for i in range(2,N+1):
        dp[i] = min(dp[i-1],dp[i-2]) + p[i]
    return dp[N]
# print(climbstair4(3,[0,1,2,3]))
# 版本五：一次迈1~2步，最小化cost，返回路径
def climbstair5(N,p):
    dp = [None]*(N+1)
    dp[0] = 1
    dp[1] = p[1]
    path = set()
    for i in range(2,N+1):
        dp[i] = min(dp[i-1],dp[i-2]) + p[i]
        if dp[i-1] <= dp[i-2]:
            path.add(i-1)
        else:
            path.add(i-2)
    path.add(N)
    return path
# print(climbstair5(8,[0,3,2,4,6,1,1,5,3]))

#版本六：机器人走路 (0,0) -> (m,n) 只能向右或向下走一步
def robot_walk_unique_paths(m,n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0 :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0 and i == 0:
                dp[i][j] = dp[i][j-1]
    return dp[m-1][n-1]
# print(robot_walk_unique_paths(1,1))

# 版本七：有路障，二维数组里面的1为路障，0为没有路障

def robot_walk_unique_paths_with_obstacles(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 :
                dp[i][j] = 0
                continue
            if i > 0 and j > 0 :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0 and i == 0:
                dp[i][j] = dp[i][j-1]
    return dp[m-1][n-1]
# print(robot_walk_unique_paths_with_obstacles([[0,0,0,0],[0,0,1,1],[0,0,0,0]]))


# 版本八：每个位置有金币，获取最多金币
def robot_walk_unique_paths_max_profit(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m):
        for j in range(n):
            dp[i][j] = grid[i][j]
            if i > 0 and j > 0 :
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
            elif i > 0 and j == 0:
                dp[i][j] += dp[i-1][j]
            elif j > 0 and i == 0:
                dp[i][j] += dp[i][j-1]
    return dp[m-1][n-1],getpath(dp,m-1,n-1,[])

def getpath(dp, i, j, path):
    if i == 0 and j == 0:
        path.append((i, j))
        return path
    if i > 0 and j > 0:
        if dp[i - 1][j] > dp[i][j - 1]:
            getpath(dp, i - 1, j, path)
        else:
            getpath(dp, i, j - 1, path)
    elif j == 0:
        getpath(dp, i- 1, j, path)
    elif i == 0:
        getpath(dp, i, j - 1, path)
    path.append((i, j))
    return path

print(robot_walk_unique_paths_max_profit([[0,2,2,50],[3,1,1,100],[4,4,2,0]]))