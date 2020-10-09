
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#  注意：你不能在买入股票前卖出股票。
#
#  示例 1:
#
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
#  示例 2:
#
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
# 思路：
# 每天有三种选择，要么不动要么买入要么卖出，直接写暴力递归
# 递归跳出条件：
# 1.数组越界（收市），直接返回利润
# 2.股票被卖了，直接返回利润（因为最多只允许一次交易）

def boot(prices):
    if prices is None or len(prices) == 0:
        return 0
    return stocks_rec(prices,0,0,0,float('inf'),0)

# prices为股价数组，index为第几天，own表示是否持有
# profit为当前利润，buy_price记录购买价格，sell表示售出
def stocks_rec(prices,index,own,profit,buy_price,sell):
    n = len(prices)
    #满足退出条件返回利润
    if index == n or sell == 1:
        return profit
    if own == 1:
        # 要么不动，要么卖出
        if prices[index] >= buy_price:
            # 允许卖出
            return max(
            stocks_rec(prices, index + 1,1,profit,buy_price,0),
            stocks_rec(prices, index + 1,0,profit + prices[index],buy_price,1))
        else :
            # 今天股价比买入的时候小，不许卖
            return stocks_rec(prices,index+1,1,profit,buy_price,0)
    if own == 0:
        # 要么不动，要么买入
        return max(
            stocks_rec(prices,index+1,0,profit,buy_price,0),
            stocks_rec(prices,index+1,1,profit-prices[index],prices[index],0))
# print(boot([7,1,5,3,6,4]))
"""
改进
因为每天的状态只跟前一天相关，所以直接用一个一维数组存储相邻一天的状态
"""
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

# print(stocks([7,1,5,3,6,4]))

#空间复杂度O(1)的写法
# 但是这样处理 base case 很麻烦，而且注意一下状态转移方程，新状态只和相邻的一个状态有关，
# 其实不用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1):
# 这道题因为只能买入一次卖出一次，所以最简单的操作是遍历数组
# 维护最低买入价格和允许最高卖出价格的差的最大值
def maxProfit_k_1(prices):
    n = len(prices)
    #dp_i_0记录卖出价格和买入价格的最大差，初值为0
    dp_i_0 = 0
    #dp_i_1记录表示最低买入价格，初值为正无穷
    dp_i_1 = float('inf')
    for i in range(n):
        #dp_i_0记录最大利润：max(保持不变，卖出价格-买入价格)
        dp_i_0 = max(dp_i_0,prices[i] - dp_i_1)
        print("dp_i_0:",dp_i_0)
        #dp_i_1时刻更新最低买入价格
        dp_i_1 = min(dp_i_1,prices[i])
        print("dp_i_1:",dp_i_1)
        #因为dp_i_0取值依赖dp_i_1取值，这样就保证了卖出只能在买入之后
    return dp_i_0
print(maxProfit_k_1([7,1,5,3,6,4]))
