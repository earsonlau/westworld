# Problem1:
# 	Coin change
# 	Given an unlimited supply of coins of given denominations,
# 	find the total number of ways to make a change of size n.
# 	Transition function: f(n) = f(n-d_1) + f(n-d_2) + f(n-d_3) + ... + f(n-d_k),
# 	where d_1, d_2, d_3, ..., d_k are provided coin denomations.
def coinchange(n,coins):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n+1):
        # 从0到n填dp表
        for coin in coins:
            # 最后一个找给顾客的币为coin
            if i-coin >= 0:
                # 保证数组不越界
                # 找钱i的方法数+=找钱i-coin的方法数（找钱i-coin完成后再拿出一个coin就凑满了i)
                dp[i] += dp[i-coin]
    return dp[n]
# print(coinchange(4,[1,3,5,10]))

#
# Problem2:
# 	Coin change
# 	Given an unlimited supply of coins of given denominations,
# 	find the total number of ways to make a change of size n, by
# 	using excatly t coins.
# 	f(i,t) = f(i-1, t-1) + f(i-2, t-1) + f(i-3, t-1) + f(i-5, t-1)

def coinchange2(n,t,coins):
    dp = [[0 for i in range(t+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n+1):
        # 从0到n填dp表
        for j in range(t+1):
            if i > 0 and j == 0:
                dp[i][j] = 0
                continue

            if j > 0 and i == 0:
                dp[i][j] = 1
                continue
            for coin in coins:
                # 最后一个找给顾客的币为coin
                if i-coin >= 0:
                    # 保证数组不越界
                    # 找钱i的方法数+=找钱i-coin的方法数（找钱i-coin完成后再拿出一个coin就凑满了i)
                    # 找钱i使用的币数  = 找钱i-coin使用的币数 + 1
                    dp[i][j] += dp[i-coin][j-1]
    return dp[n][t]
# print(coinchange2(4,2,[1,3,5,10]))

# Problem3:
# 	Coin change
# 	Given an unlimited supply of coins of given denominations,
# 	find the total number of ways to make a change of size n, by
# 	using an even number of  coins.
# 	f(i,0) = f(i-1, 1) + f(i-2, 1) + f(i-3, 1) + f(i-5, 1)
#   f(i,1) = f(i-1, 0) + f(i-2, 0) + f(i-3, 0) + f(i-5, 0)
def coinchange3(n,coins):
    dp = [[0 for i in range(2)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n+1):
        # 从0到n填dp表
            for coin in coins:
                # 最后一个找给顾客的币为coin
                if i-coin >= 0:
                    # 保证数组不越界
                    # 找钱i的方法数+=找钱i-coin的方法数（找钱i-coin完成后再拿出一个coin就凑满了i)
                    # 找钱i使用的币数  = 找钱i-coin使用的币数 + 1
                    dp[i][0] += dp[i-coin][1]
                    dp[i][1] += dp[i-coin][0]
    return dp[n][1]
# print(coinchange3(4,[1,3,5,10]))

# https://github.com/andreygrehov/dp/blob/master/lecture15/coin_change_unique_ways.go
# Problem 4
# Problem:
# 	Coin change
# 	Given an unlimited supply of coins of given denominations,
# 	find the unique number of ways to make a change of size n.
# 	Denominations:
# 	coins = [1, 2, 3, 5]
# 	Transition function:
# 	i >= 1: f[i][1] = f[i-1][1]
# 	i >= 2: f[i][2] = f[i-1][1] + f[i-2][2]
# 	i >= 3: f[i][3] = f[i-1][1] + f[i-2][2] + f[i-3][3]
# 	i >= 5: f[i][5] = f[i-1][1] + f[i-2][2] + f[i-3][3] + f[i-5][5]
# */
# 要求不同的方法数，比如{1,1,2} {1,2,1} {2,2,1}将被视为同一方法{2,2,1}
# 为了实现这种相同方法的合并，我们使用一个技巧： 只取币面值单调不增的找钱方法，以保证不重复
# 我们使用二维dp表，
# dp[i][j]=我们要找钱i的总方法数，且满足：最后给出的币面值<=j
# dp[i][0] 表示我们要找钱i,但是最后给出的币面值<=0，显然i>0时没有办法，方法数为0 i=0时 方法数为1

# 转移方程 i>=1, f[i][1] = f[i-1][1]的含义是:
# 我们最后给出的币面值<=1，要找给顾客i元.方法只包括找i-1元时最后给出币面值<=1的情况（这样找i元最后给出币<=1保证了不增），所以是 f[i-1][1]+f[i-0][0]

# 转移方程 i>=2, f[i][2] = f[i-1][1]+f[i-2][2]的含义是:
# 我们最后给出的币面值<="2"，要找给顾客i元，
# 方法只包括找i-1元时最后给出币面值<=1的情况（这样找i元最后给出币<=1保证了不增）和找i-2元时最后给出币面值<=2的情况（这样找i元最后给出币<=2保证了不增），
# 所以是 f[i-1][1]+f[i-2][2]

# 转移方程 i>=3, f[i][3] = f[i-1][1] + f[i-2][2] + f[i-3][3]的含义是:
# 我们最后给出的币面值<="3"，方法只包括找i-1元时最后给出币面值<=1的情况（这样找i元最后给出币<=1保证了不增）
# 和找i-2元时最后给出币面值<=2（这样找i元最后给出币<=2保证了不增）
# 和找i-3元时最后给出币面值<=3的情况（这样找i元最后给出币<=3保证了不增）
# ... 每个转移方程都保证每一个子情况给出的方法都是单调不增的

def coinchange4(n,coins):
    dp = [[0 for i in range(len(coins))] for j in range (n+1)]
    # dp[i][j]表示最后给出的币是coins[j]，总找钱数为i的方法数
    for i in range(len(coins)):
        # i是coins的下标
        # base case：
        # 需要找钱0元，只有"给出0个coin"一种解法
        dp[0][i] = 1
    for i in range(n+1):
        for j in range(len(coins)):
            for k in range(j+1):
                if i - coins[k] < 0 :
                    continue
                dp[i][j] += dp[i-coins[k]][k]
    return dp[n][len(coins)-1]
print(coinchange4(3,[1,2,3,5]))

