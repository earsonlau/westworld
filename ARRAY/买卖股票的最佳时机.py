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