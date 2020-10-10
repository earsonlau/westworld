# 假设有排成一行的N个位置，记为1一N，N一定大于或等于2
# 开始时机器人在其中的M位置上（M一定是1...N中的一个）
# 如果机器人来到1位置，那么下一步只能往右来到2位置
# 如果机器人来到N位置，那么下一步只能往左来到N一1位置，
# 如果机器人来到中间位置，那么下一步可以往左走或者往右走；
# 规定机器人必须走K步，最终能来到p位置（p也是1、N中的一个）的方法有多少种
# 给定四个参数N、M、K、P,返回方法数。
def ways1(N,M,K,P):
    #參數無效直接返回0
    if N< 2 or K < 1 or M < 1 or M > N or P < 1 or P > N :
        return 0
    #总共N个位置，从M出发，还剩下K步要走，返回最终能达到P的方法数
    return walk(N,M,K,P)

# N: 位置为1-N，可变
# cur: 当前在位置cur，可变
# rest: 还剩下rest步没有走，可变
# P: 最终目标是P，固定
def walk(N,cur,rest,P):
    #如果最后没有剩余步数了，当前cur的位置就是最终位置
    # 如果最终位置停留在P，那么之前的移动是有效的
    # 如果最终位置没有停留在P，那么之前的移动是无效的
    if rest == 0:
        return 1 if cur == P else 0
    #如果还有rest步要走，而当前的cur位置在1位置，那么当前这步只能从1走向2
    #后续的过程就是 来到2位置上 还剩下rest-1步要走
    if cur == 1:
        return walk(N,2,rest-1,P)

    #如果还有rest步要走，而当前的cur位置在N位置，那么当前这步只能从N走向N-1
    #后续的过程就是 来到N-1位置上 还剩下rest-1步要走
    if cur == N:
        return walk(N,N-1,rest-1,P)

    #w不在边界上，可以往左走也可以往右走
    return walk(N,cur-1,rest-1,P) + walk(N,cur+1,rest-1,P)

def waysCache(N,M,K,P):
    #參數無效直接返回0
    if N< 2 or K < 1 or M < 1 or M > N or P < 1 or P > N :
        return 0
    dp = [[-1]*(K+1)]*(N+1) #dp表所有值设成-1.表示所有参数组合都还没缓存。
    #总共N个位置，从M出发，还剩下K步要走，返回最终能达到P的方法数
    return walk(N,M,K,P,dp)

#把所有cur和rest的组合，返回的结果存入缓存中。故dp表的行数为所有可能的cur取值总数，列数为rest可能取值总数
def walkCache(N, cur, rest, P, dp):
    #有缓存就用缓存
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    # 如果最后没有剩余步数了，当前cur的位置就是最终位置
    # 如果最终位置停留在P，那么之前的移动是有效的
    # 如果最终位置没有停留在P，那么之前的移动是无效的
    if rest == 0:
        dp[cur][rest] = 1 if cur == P else 0
        return dp[cur][rest]
    # 如果还有rest步要走，而当前的cur位置在1位置，那么当前这步只能从1走向2
    # 后续的过程就是 来到2位置上 还剩下rest-1步要走
    if cur == 1:
        dp[cur][rest] = walk(N, 2, rest - 1, P,dp)
        return dp[cur][rest]
    # 如果还有rest步要走，而当前的cur位置在N位置，那么当前这步只能从N走向N-1
    # 后续的过程就是 来到N-1位置上 还剩下rest-1步要走
    if cur == N:
        dp[cur][rest] = walk(N, N - 1, rest - 1, P,dp)
        return dp[cur][rest]
    # w不在边界上，可以往左走也可以往右走
    dp[cur][rest] = walk(N, cur - 1, rest - 1, P,dp) + walk(N, cur + 1, rest - 1, P,dp)
    return dp[cur][rest]
