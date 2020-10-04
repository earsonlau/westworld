#给定一个数字字符串，转成大写字母
#1对应A 2对应B 26对应Z
#比如给'111',可以转成'AAA','AK','KA'

def convert_to_letter(str):
    if len(str) == 0:
        return 0
    str= list(str)
    return process(str,0)

#str[0..i-1]已经转化完成，现在要计算str[i]有多少种转化结果
def process(str,i):
    if i == len(str):
        return 1
    if str[i] == '0':
        return 0
    #str[i]不是'0'
    if str[i] == '1':
        res = process(str,i+1)#i自己单独转化，后续有多少种方法
        if i + 1 < len(str):
            #i和i+1一起转化，后续有多少种方法
            res += process(str,i+2)
        return res
    if str[i] == '2':
        res = process(str,i+1)
        if str[i+1] - '0' <= 6:
            res += process(str,i+2)
        return res
    if str[i] - '0' >= 3:# str[i] == '3' ~ '9'
        res = process(str,i+1)
        return res
# print(convert_to_letter('111'))

#改动态规划
def dpway(string):
    if len(string) == 0:
        return 0
    str= list(string)
    N = len(str)
    dp = [0]*(N+1)
    dp[N] = 1
    for i in range(N-1,-1,-1):
        #str[i]不是'0'
        if str[i] == '1':
            dp[i] = dp[i+1]#i自己单独转化，后续有多少种方法
            if i + 1 < len(str):
                #i和i+1一起转化，后续有多少种方法
                dp[i] += dp[i+2]

        if str[i] == '2':
            dp[i]= dp[i+1]
            if str[i+1] - '0' <= 6:
                dp[i]+=dp[i+2]

        if int(str[i]) - int('0') >= 3:# str[i] == '3' ~ '9'
            dp[i]=dp[i+1]
    return dp[0]
print(dpway("111"))