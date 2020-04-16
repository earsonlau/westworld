# 如果 k 为正无穷，那么就可以认为 k 和 k - 1 是一样的。可以这样改写框架：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
#             = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
#
# 我们发现数组中的 k 已经不会改变了，也就是说不需要记录 k 这个状态了：
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])



def maxProfit_k_inf(prices):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = -float('inf')
    for i in range(n):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0,dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1,tmp -prices[i])
    return dp_i_0
