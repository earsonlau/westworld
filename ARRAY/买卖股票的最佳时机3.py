def maxProfit_k_2(prices):
    dp_i10 = 0
    dp_i11 = -float("inf")
    dp_i20 = 0
    dp_i21 = -float("inf")
    for price in prices:
        dp_i20 = max(dp_i20, dp_i21 + price)
        dp_i21 = max(dp_i21, dp_i10 - price)
        dp_i10 = max(dp_i10, dp_i11 + price)
        dp_i11 = max(dp_i11, -price)
    return dp_i20