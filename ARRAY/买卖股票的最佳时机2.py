# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#  示例 1:
#  输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#
#  示例 2:
#  输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#  示例 3:
#
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#  提示：
#
#  1 <= prices.length <= 3 * 10 ^ 4
#  0 <= prices[i] <= 10 ^ 4
#
#  Related Topics 贪心算法 数组

#每天有三种选择，要么不动要么买入要么卖出，直接写暴力递归

def boot(prices):
    if prices is None or len(prices) == 0:
        return 0
    return stocks_rec(prices,0,0,0,float('inf'))

def stocks_rec(prices,index,own,profit,buy_price):
    n = len(prices)
    if index == n:
        return profit
    if own == 1:
        # 要么不动，要么卖出
        if prices[index] >= buy_price:
            # 允许卖出
            return max(
            stocks_rec(prices, index + 1,1,profit,buy_price),
            stocks_rec(prices, index + 1,0,profit + prices[index],buy_price))
        else :
            # 今天股价比买入的时候小，不许卖
            return stocks_rec(prices,index+1,1,profit,buy_price)
    if own == 0:
        # 要么不动，要么买入
        return max(
            stocks_rec(prices,index+1,0,profit,buy_price),
            stocks_rec(prices,index+1,1,profit-prices[index],prices[index]))
# print(boot([7,1,5,3,6,4]))

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


#空间复杂度O(1)的写法
# 但是这样处理 base case 很麻烦，而且注意一下状态转移方程，新状态只和相邻的一个状态有关，
# 其实不用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1):
# 这道题因为支持多次买入卖出，所以最简单的操作是遍历数组
# 维护新的最低买入价格和新的允许最高卖出价格的差的最大值
def maxProfit_k_1(prices):
    n = len(prices)
    #dp_i_0记录卖出价格和买入价格的最大差，初值为0
    dp_i_0 = 0
    #dp_i_1记录表示最低买入价格，初值为正无穷
    dp_i_1 = float('inf')
    for i in range(n):
        print("第",i,"天：")
        # tmp记录到第i天可以用来买股票的钱
        tmp = dp_i_0
        #dp_i_0记录最大利润：max(保持不变，卖出价格-买入价格)
        dp_i_0 = max(dp_i_0,prices[i] - dp_i_1)
        print("dp_i_0:",dp_i_0)
        #dp_i_1时刻更新最低买入价格：min(保持不变，(-1)*(买股票后还剩下的钱))
        #这样更新的话，每次刷新dp_i_0就能把买股票后剩的钱也算上。保证是全局的收益。
        dp_i_1 = min(dp_i_1,-(tmp-prices[i]))
        print("dp_i_1:",dp_i_1)
        #因为dp_i_0取值依赖dp_i_1取值，这样就保证了卖出只能在买入之后
    return dp_i_0
print(maxProfit_k_1([7,1,5,3,6,4]))
