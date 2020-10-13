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
print(coinchange2(4,2,[1,3,5,10]))

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
print(coinchange3(4,[1,3,5,10]))


