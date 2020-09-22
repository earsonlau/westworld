# # # 915题库
# #
# # 1. 有3个数据a,b,c 由键盘输入 从小到大排序。
# def abc_rank():
#     a = input("please input the first number:")
#     b = input("please input the second number:")
#     c = input("please input the third number:")
#     print("the thing you input:",a,',',b,',',c)
#     nums = []
#     nums.append(a)
#     nums.append(b)
#     nums.append(c)
#     nums.sort()
#     print("the ranked result is :",nums)
# # abc_rank()
#
# # 2. 给一个不多于5位的正整数，要求：
# #    1. 求出是几位数
# #    2. 分别输出每一位数字
# #    3. 按逆序输出各位数字，例如原数位123，输出321
#
# def reverse_output(num):
#     #求位数
#     count =len(str(num))
#     print("bit count:",count)
#     #求每位数字'
#     list1 = []
#     for i in range(count):
#         list1.append(num%10)
#         num = num // 10
#     print("every single bit:",list1)
#     #逆序输出
#     res = ""
#     for i in list1:
#         res += str(i)
#     print("reverse print",res)
# # reverse_output(123)
#
# # 3. 编写程序，将20个数读入计算机，并统计出其中正数、负数和零的个数。
# def count_pos_neg_zeros():
#     nums = []
#     i = 0
#     while(1):
#         if i == 5:
#             break
#         print("please input the ",i,"th number:")
#         elem = input()
#         if elem.lstrip('-').replace('.','',1).isdigit():
#             nums.append(elem)
#             i += 1
#             continue
#         else:
#             print("plz input a num!")
#             continue
#     print(nums)
#     pos_count = 0
#     neg_count = 0
#     zero_count = 0
#     for i in nums:
#         if float(i) > 0:
#             pos_count += 1
#             continue
#         elif float(i) < 0:
#             neg_count += 1
#             continue
#         zero_count += 1
#     print("正数个数：",pos_count)
#     print("负数个数：", neg_count)
#     print("零个数：", zero_count)
# # count_pos_neg_zeros()
#
# # 4. 打印所有的水仙花数
#
# def narcissus():
#     print("输出所有的水仙花数")
#     for i in range(100001):
#         temp = i
#         sum = 0
#         bit_count = len(str(i))
#         while temp:
#             sum += (temp % 10) ** bit_count #每位数字都求以该数字的总位数为幂的乘方结果
#             temp //= 10 #从个位数取到第一位
#         if sum == i: #满足水仙花数的定义
#             print(i,end=' ')
#     return 1
# # narcissus()
#
# # 5. 将一组数据存放在一维数组中，并排序，从键盘输入一个数，要求按原顺序将它插入到数组合适的位置上
# def insert_num():
#     array1 = [1,3,2,5,4]
#     array1.sort()
#     while(1):
#         num = input("plz input a number:")
#         if not num.lstrip('-').replace('.', '', 1).isdigit():
#             print("plz input a number!")
#             continue
#         break
#     num = int(num)
#     # print(num)
#     # print(array1[0])
#     if num < array1[0]:
#         array1.insert(0,num)
#         print(array1)
#         return 1
#     if num > array1[len(array1)-1]:
#         array1.insert(len(array1), num)
#         print(array1)
#         return 1
#
#     for i in array1:
#         if num > i:
#             print("no good")
#             continue
#         else:
#             array1.insert(array1.index(i),num)
#             break
#     return 1
#
# # insert_num()
# # 6. 输入一串字符串，以"$"结束，分别统计其中数字字符0,1,2,...,9出现的次数。
# def count_nums():
#     str1 = input("input a string of number and end with $:")
#     print(str1)
#     list1 = []
#     for i in range(10):
#         list1.append(0)
#     for i in str1:
#         if i == '$':
#             break
#         list1[int(i)] += 1
#     for i in range(len(list1)):
#         print(i,list1[i])
# # count_nums()
#
# # 7. 输入一串字符串，以"$"结束，分别统计其中大写字母出现的次数，并按字母出现的次数输出
# def count_nums():
#     str1 = input("input a string of char and end with $:")
#     print(str1)
#     #用字典
#     dict1 = {}
#     for i in str1:
#         if i == '$':
#             break
#         if 'A' <= i <= 'Z':
#             if i in dict1.keys():
#                 dict1[i] += 1
#             else:
#                 dict1[i] = 1
#     print(dict1)
#     return 1
# # count_nums()
#
# # 8. 用筛选法求100以内的素数
# def primes(n):
#     #生成2到n之间的所有整数
#     numbers = set(range(2,n))
#     #最大数的平方根，以及小于该数字的所有素数
#     m = int(n ** 0.5) + 1
#     prime_less_than_m = [p for p in range(2,m)
#                          if 0 not in [ p%d for d in range(2,int(p**0.5) + 1 )]]
#     #遍历最大整数平方根之内的所有素数
#     for p in prime_less_than_m:
#         for i in range(2,n // p + 1):
#             #干掉p的倍数
#             numbers.discard(i*p)
#     return numbers
# # print(primes(1000))
#
# # 9. 用冒泡或选排对20个数据进行排序后输出，并给出每个元素原来的位置
# def bb_sort_nums(nums):
#     #bubble sort
#     I = []
#     for i in range(len(nums)):
#         I.append(i)
#     for i in range (len(nums)):
#         for j in range(len(nums)-1,i,-1):#j移动的方向和要和i相反才能实现后面的小数字冒泡冒到前面
#             if nums[j] < nums[j-1]:
#                 nums[j-1],nums[j] = nums[j],nums[j-1]
#                 I[j-1],I[j] = I[j],I[j-1]
#     print("sorted result:",nums)
#     print("original index",I)
#     return 1
# # nums = [1, 17, 19, 23, 29, 31, 2, 5, 7, 11, 1, 3, 37, 41, 43, 47]
# # bb_sort_nums(nums)
#
# #选排
# def select_sort_nums(nums):
#     I = []
#     for i in range(len(nums)):
#         I.append(i)
#     for i in range(len(nums)):
#         min = i
#         for j in range(i+1,len(nums)):
#            if (nums[j] < nums[min]):
#                min = j
#         if (min != i):
#             t = nums[i]
#             nums[i] = nums[min]
#             nums[min] = t
#             I[i],I[min] = I[min],I[i]
#     print("sorted result:",nums)
#     print("original index",I)
#     return 1
#
# # nums = [1, 17, 19, 23, 29, 31, 2, 5, 7, 11, 1, 3, 37, 41, 43, 47]
# # select_sort_nums(nums)
#
# # 10. 把20个元素读入数组，找最大值和最小值并输出值与下标。最后将数组各元素按从大到小重新排列，输出。
# def sort_sunny(nums):
#     max = nums[0]
#     min = nums[0]
#     max_index = 0
#     min_index = 0
#     for i in range(len(nums)):
#         if nums[i] > max:
#             max = nums[i]
#             max_index = i
#         if nums[i] < min:
#             min = nums[i]
#             min_index = i
#     print("max:",max,"index:",max_index)
#     print("min:",min,"index:",min_index)
#
#
#     for i in range (len(nums)):
#         for j in range(len(nums)-1,i,-1):#j移动的方向和要和i相反才能实现后面的小数字冒泡冒到前面
#             if nums[j] > nums[j-1]:
#                 nums[j-1],nums[j] = nums[j],nums[j-1]
#     print("sorted result:",nums)
#
# # nums = [1, 17, 19, 23, 29, 31, 2, 5, 7, 11, 1, 3, 37, 41, 43, 47]
# # sort_sunny(nums)
#
# # 11. 编写程序，不用标准函数而把两个字符串连接。
# def connect_string(str1,str2):
#     return print(str1+str2)
#
# # 12. 编写程序，求字符串长度，并将长度打印。
# def string_length(str):
#     return print(len(str))
#
# # 13. 编写排序程序，用数组排20个输入的数。
# def sort_leaf():
#     pass
#
# # 14. 从键盘读取10个整型数字，去掉重复的，剩下的从大到小输出
# def remove_dup(nums):
#     nums.sort(reverse =True)
#     res = []
#     for i in nums:
#         if i in res:
#             continue
#         else:
#             res.append(i)
#     print(res)
#
# # nums = [1, 1, 1, 3, 9, 3, 2, 5, 7, 11, 1, 3, 37, 41, 43, 47]
# # remove_dup(nums)
#
# # 15. 写个函数，从键盘读个字符串反序存放，并在主函数中输入输出该字符串
# def reverse_string(str):
#     if str == "":
#         return str
#     else:
#         return reverse_string(str[1:])+str[0]
# # print(reverse_string("abcdef"))
#
#
#
# # 16. 输入5个大学生4门功课的成绩，然后求出：
# #     1. 每个人的总分
# #     2. 每门课程的总分
# #     3. 输入总分最高的学生的姓名和总分数
# def score():
#     nums = [[0] * 5 for row in range(4)]
#     for i in range(5):
#         for j in range(4):
#             nums[i][j] = input("plz input the ",i,"th student's",j,"th score:")
#     #now we get all the scores for everybody
#     student_score = []
#     for i in range(5):
#         student_score.append(sum(nums[i]))
#     lesson_score = []
#     for j in range(4):
#         lesson_score.append(sum(nums[j]))
#     max = student_score[0]
#     for i in range(len(student_score)):
#         if student_score[i] > max:
#             max = student_score[i]
#             index= i
#     print("max student score",max," ,name:",index)
#     return 1
#
# # 17. 编写一个函数，输入一个十进制数，输出相应的二进制、八进制、十六进制数。
#
# def dec2bin(num):
#     # dec2bin
#     l = []
#     if num < 0:
#         return '-' + dec2bin(abs(num))
#     while(1):
#         num,remainder = divmod(num,2)#模2，取一下余数并更新num为原来的1/2
#         l.append(str(remainder))#把余数存起来
#         if num == 0 :
#             return ''.join(l[::-1])#反转输出
#
# def dec2oct(num):
#     # dec2oct
#     l = []
#     if num < 0:
#         return '-' + dec2oct(abs(num))
#     while (1):
#         num, remainder = divmod(num, 8)  # 模2，取一下余数并更新num为原来的1/2
#         l.append(str(remainder))  # 把余数存起来
#         if num == 0:
#             return ''.join(l[::-1])  # 反转输出
#
#
# base = [str(x) for x in range(9)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
# def dec2hex(num):
# # dec2hex
#     l = []
#     if num < 0:
#         return '-' + dec2hex(abs(num))
#     while (1):
#         num, remainder = divmod(num, 16)  # 模2，取一下余数并更新num为原来的1/2
#         l.append(base[remainder])  # 把余数存起来
#         if num == 0:
#             return ''.join(l[::-1])  # 反转输出
#
#
# def dec_to_bin_oct_hex(num):
#     print('bin:', dec2bin(num))
#     print('bin:',oct = dec2oct(num))
#     print('bin:',hex = dec2hex(num))
#     return 1
#
# # 18. 用递归法，求n!
# def cal_n_step_product(n):
#     if n == 0:
#         return 1
#     return n*(cal_n_step_product(n-1))
#
# # print(cal_n_step_product(3))
#
# # 19. 写个函数，输出数n从右边开始的第k个数字的值
# def kth_num_from_right(n,k):
#     if k >= len(str(n)):
#         print("k is too large!")
#         return 0
#     for i in range(k):
#         res = n % 10
#         n = n // 10
#     return print(res)
# kth_num_from_right(1234567,4)
#
#
# # 20. 写个回答星期几的函数。函数三个参分别为年月日，输出“星期__”
# def what_the_day():
#     import calendar
#     from calendar import *
#     import datetime
#     y = input('请输入年份')
#     m = input('请输入月份')
#     d = input('请输入日')
#     lis = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日',]
#     dic = dict(enumerate(lis))
#     if y.isdigit() and m.isdigit() and d.isdigit() and 1<=int(m)<=12 and 1<=int(d)<=31 :
#         w = weekday(int(y),int(m),int(d))
#         print(dic[w])

# 21. 求给定5个数的最大值
def get_max(nums):
    max = nums[0]
    for i in range(len(nums)):
        if i > max:
            max = nums[i]
    print('the max number is :',max)
    return 1

# get_max([1,2,3,4,5])


# 22. 用递归的方式写程序，输入一个非负整数，输出这个数的逆序十进制数
# def reverse_num(num):
#     num = str(num)
#     if len(num) == 1 :
#         if num == '0' :
#             return ''
#         else:
#             return num
#     return reverse_num(num[1:])+num[0]
#
# print(reverse_num(12340))
# 23. 设计下面两个函数：
# #     1. 函数readoctal()，读入八进制序列，转十进制正整数
# def readoctal(num):
#     if num <0:
#         return '-'+readoctal(abs(num))
#     # num0,remainder = divmod(num,8)
#     # res = num0*10+remainder
#     # return res
#     num = str(num)
#     sum = 0
#     for i in range(len(num)):
#         sum += int(num[len(num) - 1 - i]) * pow(8, i)
#     return sum
# print(readoctal(13))

#     2. 函数writeoctal(), 将十进制正整数转换成相应的八进制数字序列，并打印出来

# def dec2oct(num):
#     # dec2oct
#     l = []
#     if num < 0:
#         return '-' + dec2oct(abs(num))
#     while (1):
#         num, remainder = divmod(num, 8)  # 模8，取一下余数并更新num为原来的1/8
#         l.append(str(remainder))  # 把余数存起来
#         if num == 0:
#             return ''.join(l[::-1])  # 反转输出
# 24. 编程实现查找字符串s2在字符串s1中第一次出现的位置，若找到则返回位置，否则返回0
# def find_string(s1,s2):
    #暴力匹配
#     offset= 0
#     for i in range(len(s1)-len(s2)+1):
#         if s1[i] == s2[0]:
#             offset = i
#             for j in range(1,len(s2)):
#                 if s1[i+j] != s2[j]:
#                     break
#                 continue
#             if j == len(s2)-1:
#                 return offset
#         continue
#     return -1
# print(find_string("hello","ll"))
# 25. 函数expand(s,t) 在把字符串s复制到字符串t时，将其中的换行符和制表符转换成可见的转义字符，即用\n表示换行符，用\t表示制表符，用指针实现。
# def expand(s,t):
#     #naive copy
#     # for i in range(len(s)):
#     #     t+=s[i]
#     # return t
#     #smart copy
#     for i in range(len(s)):
#         if s[i] == '\n':
#             t += '\\'
#             t += 'n'
#             continue
#         elif s[i] == '\t':
#             t += '\\'
#             t += 't'
#             continue
#         else :
#             t += s[i]
#             continue
#     return t
# print(expand("abc\n",""))
# 26. 写一个函数getint，它把输入的一串数字字符转换为整数。
# def getint(str):
#     res = 0
#     for i in range(len(str)):
#         res += int(str[i])*(10**(len(str)-1-i))
#     return res
# print(getint('12345'))

# # 27. 写一个函数squeeze(s1,s2),它删去字符串s1中与字符串s2中任意字符相匹配的字符。
# def squeeze(s1,s2):
#     res = ''
#     for i in s1:
#         if i not in s2:
#           res+= i
#         else:
#             continue
#     return res
# # print(squeeze('1213','12'))
#
# # 28. 用指针的方法实现三个字符串的排序输出，排序的规则是：按字符比较ascii码。
# def cmp_2str(s1,s2):
#     len_cmp = min(len(s1),len(s2))
#     for i in range(len_cmp):
#         if s1[i] == s2[i]:
#             continue
#         elif s1[i]>s2[i]:
#             return 1
#         else:
#             return 2
#     if len(s1) >= len(s2):
#         return 1
#     else :
#         return 2
# def sort_string(s1,s2,s3):
#     #拆成两个函数cmp和sort来写。
#     res = []
#     if cmp_2str(s1,s2)  == 1 and cmp_2str(s1,s3) == 1 :
#         res.append(s1)
#         if cmp_2str(s2,s3) == 1:
#             #s1>s2>s3
#             res.append(s2)
#             res.append(s3)
#         else:
#             #s1>s3>s2
#             res.append(s3)
#             res.append(s2)
#
#     if cmp_2str(s2,s1)  == 1 and cmp_2str(s2,s3) == 1 :
#         res.append(s2)
#         if cmp_2str(s1,s3) == 1:
#             #s2>s1>s3
#             res.append(s1)
#             res.append(s3)
#         else:
#             #s2>s3>s1
#             res.append(s3)
#             res.append(s1)
#
#
#     if cmp_2str(s3, s1) == 1 and cmp_2str(s3, s2) == 1:
#         res.append(s3)
#         if cmp_2str(s1, s2) == 1:
#             # s3>s1>s2
#             res.append(s1)
#             res.append(s2)
#         else:
#             # s3>s2>s1
#             res.append(s2)
#             res.append(s1)
#     return res
# # 29. 有一个字符串，包含n个字符。写一个函数，将此字符串中从第m个字符开始的全部字符复制成为另一个字符串。
# def copy_from_m(s,m):
#     return s[m:]
#     pass

# 30. 用指针数组和指向指针的指针的方法实现对10个字符串的排序，输出结果
# pass
# 31. 编写函数实现自己的strcat(), 实现两个字符串的合并。
def strcat(s1,s2):
    return s1+s2
# 32. 定义一个结构体变量（包括年月日），计算该日在本年是第几天。注意闰年的问题。
# class ymd:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def calculate(self):
#         month_day_list_not_run = []
#         montH_day_list_run = []
#         if self.year % 400 == 0:#is run year
#             #use run table
#             #use non run table
#             pass
# 33. 使用结构体数组存放三个学生的学号、姓名、性别和三门单科成绩。输出总分最高的学生以及有一科及以上不及格的学生的各项数据
class students:
    def __init__(self,stu_no,name,gender):
        self.stu_no = stu_no
        self.name = name
        self.gender = gender

    def get_score(self,chinese,math,english):
        self.chinese = chinese
        self.math = math
        self.english = english

    def get_total_score(self):
        self.total = self.chinese + self.math + self.english
        return self.total

    def get_min_score(self):
        self.min_socre = min(self.chinese,self.math,self.english)
        return self.min_socre

def get_max_ts_student(stus):
    max = stus[0].get_total_score()
    stu = stus[0]
    for i in stus:
        if i.get_total_score() > max :
            max = i.get_total_score()
            stu = i
    return stu

def get_fail_student(stus):
    fail_guys= []
    for i in stus:
        if i.get_min_score() < 60:
            fail_guys.append(i)
    print('Guys who failed in course:')
    for j in fail_guys:
        print("student_no:",j.stu_no,",name:",j.name,", total_score:",j.get_total_score(),", min_score:",j.get_min_score())



tom = students(1,'tom','m')
tom.get_score(80,100,100)
jerry = students(2,'jerry','m')
jerry.get_score(99,99,99)
doggie = students(3,'doggie','m')
doggie.get_score(38,98,98)
stus = [tom,jerry,doggie]
# nerd = get_max_ts_student(stus)
# print(stus[0].name)
# print(stus[1].english)
# print('Guy who get max total score is ',nerd.name,', with',nerd.get_total_score())
get_fail_student(stus)
