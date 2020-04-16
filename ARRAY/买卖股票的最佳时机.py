# DP

def stocks(prices):
    n = len(prices)
    dp = [[0]*2]*n

    for i in range(n):
        if (i - 1 == -1):
            dp[i][0] = 0
            # // 解释：
            # //   dp[i][0]
            # // = max(dp[-1][0], dp[-1][1] + prices[i])
            # // = max(0, -infinity + prices[i]) = 0
            dp[i][1] = -prices[i]
            # //解释：
            # //   dp[i][1]
            # // = max(dp[-1][1], dp[-1][0] - prices[i])
            # // = max(-infinity, 0 - prices[i])
            # // = -prices[i]
            continue

        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[n - 1][0]

print(stocks([7,1,5,3,6,4]))

#空间复杂度O(1)的写法
# 但是这样处理 base case 很麻烦，而且注意一下状态转移方程，新状态只和相邻的一个状态有关，
# 其实不用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1):

def maxProfit_k_1(prices):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = -float('inf')
    for i in range(n):
        dp_i_0 = max(dp_i_0,dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1,-prices[i])
    return dp_i_0
