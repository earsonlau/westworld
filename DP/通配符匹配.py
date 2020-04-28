# 1. 通配符匹配
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false
#
# 双指针贪心算法
#
def isMatch(s,p):
    if (p is None or len(p)==0):
        return s == None or len(s) == 0
    i = 0
    j = 0
    i_start = -1
    j_start = -1
    slen = len(s)
    plen = len(p)
    # 判断s的所有字符是否匹配
    while i < slen:
        #三种匹配成功情况以及匹配失败返回False
        if j < plen and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j <plen and p[j] == '*':
            i_start = i
            j_start = j
        elif i_start > -1 :
            i_start += 1
            i = i_start
            j = j_start + 1
        else:
            return False
    # s中的字符都判断完毕，则认为s为空，此时需要p为空或者p中只剩下星号的时候才能成功匹配
    # 如果p中剩余的都是*,则可以移除剩余的*
    while (j < plen and p[j] == '*'):
        j += 1
    return j == plen


#
# 动态规划
#
#
def isMatch(s,p):
    if (p is None or len(p)==0):
        return s == None or len(s) == 0
    i = 0
    j = 0
    i_start = -1
    j_start = -1
    slen = len(s)
    plen = len(p)
    dp = [[False for _ in range (plen+1)] for _ in range(slen+1)]
    #初始化dp数组,dp[1][0]~dp[len(s)][0]默认False
    dp[0][0] = True
    #dp[0][1]~dp[0][len(p)]只有p的j字符以及前面所有字符都为'*'才为True
    for j in range(1,plen+1):
        dp[0][j] = (p[j-1] == '*' and dp[0][j-1])
    #填写dp数组剩余部分
    for i in range(1,slen+1):
        for j in range(1,plen+1):
            si = s[i - 1]
            pj = p[j - 1 ]
            if (si == pj or pj == '?'):
                dp[i][j] = dp[i-1][j-1]
            elif pj == '*':
                dp[i][j] = (dp[i-1][j] or dp[i][j-1])
    return dp[slen][plen]