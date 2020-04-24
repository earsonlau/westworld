# 1.
# 最长回文子串问题
#
# 给定一个字符串
# s，找到
# s
# 中最长的回文子串。你可以假设 s
# 的最大长度为
# 1000。
#
# 示例
# 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"
# 也是一个有效答案。
# 示例
# 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
# key：双指针
#
# 寻找回文串的问题核心思想是：从中间开始向两边扩散来判断回文串。
#
# 回文串的长度可能是奇数也可能是偶数, 所以
#
# for 0 <= i < len(s):
#     找到以
#     s[i]
#     为中心的回文串
#     找到以
#     s[i]
#     和
#     s[i + 1]
#     为中心的回文串
#     更新答案
#
# 先要实现一个函数来寻找最长回文串
#
# string
# palindrome(string & s, int
# l, int
# r){
#   // 防止索引越界
# while (l >= 0 & & r < s.size() & & s[l] == s[r]){
# // 向两边展开
# l--;
# r++;
# }
# // 返回以
# s[l]
# 和
# s[r]
# 为中心的最长回文串
# return s.substr(l + 1, r - l - 1)
# }
#
# 传入两个指针
# l
# 和
# r
# 的目的：同时处理回文串长度为奇数和偶数的情况
#
# for 0 <= l << len(s):
# # 找到以s[i] 为中心的回文串
#     palindrome(s, i, i)
# # 找到 以s[i] 和 s[i+1] 为中心的回文串
# palindrome(s, i, i + 1)
# 更新答案
#
# 完整代码:

# string palindrome(string s):
#     string res;
#     for(i=0; i<s.size();i++){
#         //以 s[i] 为中心的回文串
#         string s1 = palindrome(s,i,i);
#         //以 s[i] 和 s[i+1] 为中心的回文串
#         string s2 = palindrome(s,i,i+1);
#         // res = longest(res,s1,s2)
#         res = res.size() > s1.size() ? res : s1;
#         res = res.size() > s2.size() ? res : s2;
#     }
#     return res;
# }

