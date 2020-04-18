# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    window = {}#存s中每个字符出现的次数
    res = 0
    print(s)

    while right < len(s):
        c1 = s[right]
        if c1 not in window:
            print('第一次见到',c1,'!')
            window[c1] = 1
        else:
            print('又见到了',c1)
            window[c1] = window[c1] + 1
        right += 1
        print("right自增1，变成",right)
        #如果window中出现了重复字符
        #开始移动left缩小窗口
        while window[c1] > 1 :
            print("那个重复的字符回来了！就是:",c1)
            c2 = s[left]
            window[c2] = window[c2] - 1
            left += 1
            print("left自增1，变成", left)
        res = max(res,right - left)
        print("存一下最大间隔", res)
    return res

print(lengthOfLongestSubstring("abcabcbb"))