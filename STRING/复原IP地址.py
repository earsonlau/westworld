# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
def restoreIpAddresses(s):
    result = []
    ip = []
    for a in range(1,4):
    # for (int a = 1; a < 4; a++) {
        for b in range(1,4):
        # for (int b = 1; b < 4; b++) {
            for c in range(1,4):
            # for (int c = 1; c < 4; c++) {
                for d in range(1,4):
                # for (int d = 1; d < 4; d++) {
                #     /*
                #      * 1、保障下面subString不会越界
                #      * 2、保障截取的字符串与输入字符串长度相同
                #      * //1、2比较好理解，3比较有意思
                #      * 3、不能保障截取的字符串转成int后与输入字符串长度相同
                #      * 如：字符串010010，a=1，b=1，c=1，d=3，对应字符串0，1，0，010
                #      * 转成int后seg1=0，seg2=1，seg3=0，seg4=10
                #      * //所以需要下面这处判断if (ip.length() == s.length() + 3)
                #      */
                #     找到可能的长度组合abcd
                    if (a + b + c + d == len(s)):
                        n1 = int(s[0:a])
                        n2 = int(s[a:a+b])
                        n3 = int(s[a+b:a+b+c])
                        n4 = int(s[a+b+c:a+b+c+d])
                        # // 四个段数值满足0~255
                        if (n1 <= 255 and n2 <= 255 and n3 <= 255 and n4 <= 255) :
                            ip.append(str(n1))
                            ip.append(".")
                            ip.append(str(n2))
                            ip.append(".")
                            ip.append(str(n3))
                            ip.append(".")
                            ip.append(str(n4))
                            vip = "".join(ip)
                            # // 保障截取的字符串转成int后与输入字符串长度相同
                            if (len(vip) == len(s) + 3):
                                result.append(vip)
                            ip.clear()
    return result
print(restoreIpAddresses("25525511135"))
