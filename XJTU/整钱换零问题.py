def ways(arr,aim):
    if len(arr) == 0 or aim < 0:
        return 0
    return process(arr,0,aim)

#可以自由使用arr[index...] 所有的面值（均有无穷张）
def process(arr,index,rest):
    if rest < 0:
        return 0
    #rest>=0
    if index == len(arr):
        #没有货币可以选择了
        return 1 if rest == 0 else 0
    #当前有arr[index]的货币
    ways = 0
    for zhang in range(0,rest//arr[index] + 1):
        ways += process(arr,index+1,rest-zhang * arr[index])
    return ways

def memoryways(arr,aim):
    if len(arr) == 0 or aim < 0:
        return 0
    # map = {} # key:"index_rest",value:方法数
    dp = [[-1 for i in range(aim+1)] for j in range(len(arr)+1)]
    #一开始都还没计算，dp所有值均为-1
    return process2(arr,0,aim,dp)

#可以自由使用arr[index...] 所有的面值（均有无穷张）
#如果（index,rest）这一参数组合没算过，dp[index][rest] = -1
#算过的话,dp[index][rest]>-1
def process2(arr,index,rest,dp):
    if dp[index][rest] != -1:
        return dp[index][rest]
    if rest < 0:
        return 0
    #rest>=0
    if index == len(arr):
        dp[index][rest] = 1 if rest == 0 else 0
        #没有货币可以选择了
        return dp[index][rest]
    #当前有arr[index]的货币
    ways = 0
    for zhang in range(0,rest//arr[index] + 1):
        ways += process2(arr,index+1,rest-zhang * arr[index],dp)
    dp[index][rest] = ways
    return ways

def ways3(arr,aim):
    if len(arr) == 0 or aim < 0:
        return 0
    N = len(arr)
    # map = {} # key:"index_rest",value:方法数
    dp = [[0 for i in range(aim + 1)] for j in range(len(arr) + 1)]
    arr = [50,10,100]
    aim = 1000
    dp[N][0] = 1 #你取的东西已经来到N位置，那么只有说不需要其他面值了才有可能是1不然都是0
    for index in range(N-1,-1,-1):
        for rest in range(0,aim+1):
            ways = 0
            for zhang in range(0, rest // arr[index] + 1):
                ways += dp[index + 1][rest - zhang * arr[index]]
            dp[index][rest] = ways

    return dp[0][aim]

def ways4(arr,aim):
    if len(arr) == 0 or aim < 0:
        return 0
    N = len(arr)
    # map = {} # key:"index_rest",value:方法数
    dp = [[0 for i in range(aim + 1)] for j in range(len(arr) + 1)]
    arr = [50,10,100]
    aim = 1000
    dp[N][0] = 1 #你取的东西已经来到N位置，那么只有说不需要其他面值了才有可能是1不然都是0
    for index in range(N-1,-1,-1):
        for rest in range(0,aim+1):
            dp[index][rest] = dp[index+1][rest]
            if rest -arr[index] >= 0:
                dp[index][rest] += dp[index][rest-arr[index]]

    return dp[0][aim]
arr = [10,50,100]
aim = 1000
print(ways(arr,aim))
print(memoryways(arr,aim))
print(ways3(arr,aim))
print(ways4(arr,aim))
