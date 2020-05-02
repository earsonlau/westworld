# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false

#双指针，一个从前到后遍历，一个从后到前遍历
def verifypa(s):
    left = 0
    right = len(s) - 1
    if len(s)== 0 or s is None:
        return False
    while(left < len(s)):
        print(s[left])
        print(s[right])
        if (s[left].isalnum() and s[right].isalnum()):
            if(s[left].lower() != s[right].lower()):
                return False
            else:
                left += 1
                right -= 1
        elif s[left].isalnum():
            right -= 1
        else:
            left += 1
    return True
print(verifypa("A man, a plan, a canal: Panama"))
