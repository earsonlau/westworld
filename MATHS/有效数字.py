# 验证给定的字符串是否可以解释为十进制数字。
#
# 例如:
#
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
#
# 数字 0-9
# 指数 - "e"
# 正/负号 - "+"/"-"
# 小数点 - "."
# 当然，在输入中，这些字符的上下文也很重要。
#
# 更新于 2015-02-10:
# C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。
#
#
# 把当前的输入分成几类，再用几个标志位来判断当前是否合法。


# public boolean isNumber(String s) {
#     s = s.trim();
#
#     boolean pointSeen = false;
#     boolean eSeen = false;
#     boolean numberSeen = false;
#     boolean numberAfterE = true;
#     for(int i=0; i<s.length(); i++) {
#         if('0' <= s.charAt(i) && s.charAt(i) <= '9') {
#             numberSeen = true;
#             numberAfterE = true;
#         } else if(s.charAt(i) == '.') {
#             if(eSeen || pointSeen) {
#                 return false;
#             }
#             pointSeen = true;
#         } else if(s.charAt(i) == 'e') {
#             if(eSeen || !numberSeen) {
#                 return false;
#             }
#             numberAfterE = false;
#             eSeen = true;
#         } else if(s.charAt(i) == '-' || s.charAt(i) == '+') {
#             if(i != 0 && s.charAt(i-1) != 'e') {
#                 return false;
#             }
#         } else {
#             return false;
#         }
#     }
#
#     return numberSeen && numberAfterE;
# }

def isNumber(s):
    s = s.strip()
    pointSeen = False
    eSeen = False
    numberSeen = False
    numberAfterE = True
    for i in range(len(s)):
        if ('0' <= s[i] and s[i] <= '9'):
            numberSeen = True
            numberAfterE = True
        elif s[i] == '.':
            if eSeen or pointSeen:
                return False
            pointSeen = True
        elif s[i] == 'e':
            if eSeen or (not numberSeen):
                return False
            numberAfterE = False
            eSeen = True
        elif s[i] == '-' or s[i] == '+':
            if i != 0 and s[i-1] != 'e':
                return False
        else:
            return  False
    return numberSeen and numberAfterE
