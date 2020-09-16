# 1.
# a b c d 是四个0-9的数字 输出所有使得 abcd+cadb = 9102 的 abcd 数字
def plus_to_get_9102_v1():
    res = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    abcd = a*1000 + b*100 + c*10 + d
                    cadb = c*1000 + a*100 + d*10 + b
                    print (abcd)
                    if abcd + cadb  == 9102:
                        res.append(abcd)
    print(res)
    return 1

def plus_to_get_9102_v2():
    # 先给一个数字 然后输出 这个四位数字的各位
    res = []
    for abcd in range(10000):
        a = (abcd//1000) % 10
        b = (abcd//100) %10
        c = (abcd //10) %10
        d = abcd % 10
        cadb = c*1000 + a*100 + d*10 + b
        if abcd + cadb == 2222:
            res.append(str(a)+str(b)+str(c)+str(d))
    print(res)
    return 1
# plus_to_get_9102_v2()

# 2.
# 输入n组 a,b (ab均>0且小于10000) ab反转的和是和的反转 则输出a,b
# 输入：
# 第一行为n代表输入的组数
# 下面几行代表几对数组
def sum_is_reverse():
    # print("Enter your content,ctrl+D to save")
    # contents = []
    # while True:
    #     try:
    #         line = input()
    #     except EOFError:
    #         break
    #     contents.append(line)
    #     print(contents)
    contents = [3,123,456]
    n = contents[0]
    nums = contents[1:]
    for i in nums:
        for j in nums[nums.index(i):]:
            i_reverse = reverse(i)
            # print("i reverse:",reverse(i))
            j_reverse  = reverse(j)
            # print("j reverse:",reverse(j))
            # print("i_reverse + j_reverse: ",i_reverse + j_reverse )
            # print("reverse i+j: ",reverse(i+j))
            if i_reverse + j_reverse == reverse(i+j):
                print(i,j,'\n')
    return 0

def reverse(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

# sum_is_reverse()

# 3.
# 公司发礼品 有n件商品价值为a1 a2... an的不同商品  员工有200元的额度 请问共有多少种搭配
# 输入：3 代表3个商品 继续输入(150,100,50)代表价值
# 输出：4


# Given weights and values of n items,
# put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values
# and weights associated with n items respectively.
# Also given an integer W which represents knapsack capacity,
# find out the maximum value subset of val[]
# such that sum of the weights of this subset is smaller than or equal to W.
# You cannot break an item, either pick the complete item or don’t pick it (0-1 property).


# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
# def knapSack(W, wt, val, n):
# 	K = [[0 for x in range(W + 1)] for x in range(n + 1)]
#
# 	# Build table K[][] in bottom up manner
# 	for i in range(n + 1):
# 		for w in range(W + 1):
# 			if i == 0 or w == 0:
# 				K[i][w] = 0
# 			elif wt[i-1] <= w:
# 				K[i][w] = max(val[i-1]
# 					+ K[i-1][w-wt[i-1]], K[i-1][w])
# 			else:
# 				K[i][w] = K[i-1][w]
#
# 	return K[n][W]
#
# # Driver program to test above function
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print(knapSack(W, wt, val, n))

# This code is contributed by Bhavya Jain

# fiboacci number
# def fib(n):
#     #base case
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(9))

#
# def fib_dp(n):
#     fib_array = [0,1]
#     while len(fib_array) < n+1 :
#         fib_array.append(0)
#     if n <= 1:
#         return n
#     else:
#         if fib_array[n-1] == 0:
#             fib_array[n-1] = fib_dp(n-1)
#
#         if fib_array[n-2] == 0:
#             fib_array[n-2] = fib_dp(n-2)
#
#     fib_array[n] = fib_array[n-1]+fib_array[n-2]
#     return fib_array[n]
#
# print(fib_dp(9))

# Recursive Python3 program for
# coin change problem.

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def count(s, m, n ):

	# If n is 0 then there is 1
	# solution (do not include any coin)
	if (n == 0):
		return 1

	# If n is less than 0 then no
	# solution exists
	if (n < 0):
		return 0;

	# If there are no coins and n
	# is greater than 0, then no
	# solution exist
	if (m <=0 and n >= 50):
		return 0

	# count is sum of solutions (i)
	# including S[m-1] (ii) excluding S[m-1]

	return count( s, m - 1, n ) + count( s, m, n-s[m-1] )

# Driver program to test above function
arr = [50, 100, 150]
m = len(arr)
print(count(arr, m, 200))

# This code is contributed by Smitha Dinesh Semwal
# Since same suproblems are called again, this problem has Overlapping Subprolems property.
# So the Coin Change problem has both properties (see this and this) of a dynamic programming problem.
# Like other typical Dynamic Programming(DP) problems,
# recomputations of same subproblems can be avoided by constructing a temporary array table[][]
# in bottom up manner.
# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
	# We need n+1 rows as the table is constructed
	# in bottom up manner using the base case 0 value
	# case (n = 0)
	table = [[0 for x in range(m)] for x in range(n + 1)]

	# Fill the entries for 0 value case (n = 0)
	for i in range(m):
		table[0][i] = 1

	# Fill rest of the table entries in bottom up manner
	for i in range(1, n + 1):
		for j in range(m):
			# Count of solutions including S[j]
			x = table[i - S[j]][j] if i - S[j] >= 0 else 0

			# Count of solutions excluding S[j]
			y = table[i][j - 1] if j >= 1 else 0

			# total count
			table[i][j] = x + y

	return table[n][m - 1]


# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))

# This code is contributed by Bhavya Jain

# Following is a simplified version of method 2. The auxiliary space required here is O(n) only.
# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
	# table[i] will be storing the number of solutions for
	# value i. We need n+1 rows as the table is constructed
	# in bottom up manner using the base case (n = 0)
	# Initialize all table values as 0
	table = [0 for k in range(n + 1)]

	# Base case (If given value is 0)
	table[0] = 1

	# Pick all coins one by one and update the table[] values
	# after the index greater than or equal to the value of the
	# picked coin
	for i in range(0, m):
		for j in range(S[i], n + 1):
			table[j] += table[j - S[i]]

	return table[n]


# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
x = count(arr, m, n)
print(x)

# This code is contributed by Afzal Ansari