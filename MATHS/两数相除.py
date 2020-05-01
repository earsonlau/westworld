# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
#
#
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
#
#
# 提示：
#
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
def divide(dividend,divisor): #dividend分子,divisor分母
    if divisor == -1 and dividend == -float('inf'):
        return float('inf') # 溢出
    sign = 1
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        sign = -1
    if divisor == 1: return dividend
    if divisor == -1: return -dividend
    a = -dividend if dividend > 0 else dividend
    b = -dividend if dividend > 0 else dividend
    #         // 都改为负号是因为int 的范围是[2^32, 2^32-1]，如果a是-2^32，转为正数时将会溢出
    if a > b: return 0
    ans = div(a,b)
    return -ans if sign == -1 else ans

def div(a,b):
    if a > b : return 0
    count = 1
    tb = b
    while tb + tb >= a and tb + tb < 0: # 溢出之后不再小于0
        tb += tb
        count += count
        print(tb + " " + count + " " + count * b)
    return count + div(a-tb,b)
