# # 1. 反转链表
# # 双指针操作即可，一个cur和一个pre，加上一个tmp保存一下下一个要遍历的
# def reverselist(head):
#     pre = None
#     cur = head
#     while cur != None:
#         tmp = cur.next
#         cur.next =pre
#         pre = cur
#         cur = tmp
#     return pre
# # 2. 二分查找
# 
# # 3. 二叉树的先序中序后序
# # 4. 判断链表中是否有环
# # 5. 合并有序链表
# # 6. 寻找第K大
# # 7. 删除链表的倒数第k个节点
# # 8. 二叉树层次遍历
# # 8. 两个栈实现队列
# # 9. 最长公共子串
# # 10. 子数组最大累加和
# # 11. 最长递增子序列
# 

# def F_to_C(F):
#     return float((5/9)*(F-32))
# def cal():
#     for i in range(4):
#         F=input("请输入华氏温度：")
#         print((F_to_C(float(F))))
# cal()

# import math
# def earth(r):
#     print("地球的半径是：",r,"，pi的近似值是:",round(math.pi,4),"，地球的表面积是：",(4/3)*math.pi*r*r)
# earth(6371.0)

# import math
# def cal_tri():
#     a,b,c=input("请输入三条边的值\n").strip().split()
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     s = (a+b+c)/2
#     area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#     print(a,b,c,area)
# cal_tri()

import math as ma
def cal_y_z():
    x = float(input("plz input x:"))
    if x <= 2.5:
        y = x * x + 1
    else :
        y = x * x - 1
    if x < 0:
        z = -2 * x / ma.pi
    elif x == 0:
        z = 0
    else:
        z = 2 * x * ma.pi
    print(y,z)
# cal_y_z()
def primes(n):
    #生成2到n之间的所有整数
    numbers = set(range(2,n))
    #最大数的平方根，以及小于该数字的所有素数
    m = int(n ** 0.5) + 1
    prime_less_than_m = [p for p in range(2,m)
                         if 0 not in [ p % d for d in range(2,int(p**0.5) + 1 )]]
    #遍历最大整数平方根之内的所有素数
    for p in prime_less_than_m:
        for i in range(2,n // p + 1):
            #干掉p的倍数
            numbers.discard(i*p)
    return numbers
# print(primes(100))


#选排
def select_sort_nums(nums):
    I = [] # I是下标
    for i in range(len(nums)):
        I.append(i)
    for i in range(len(nums)):
        min = i
        for j in range(i+1,len(nums)):
           if (nums[j] < nums[min]):
               min = j
        if (min != i):
            nums[i],nums[min] = nums[min],nums[i]
            I[i],I[min] = I[min],I[i]
    print("sorted result:",nums)
    print("original index",I)
    return 1

# nums = [1, 17, 19, 23, 29, 31, 2, 5, 7, 11, 1, 3, 37, 41, 43, 47]
# select_sort_nums(nums)


def what_the_day():
    import calendar
    y = input('请输入年份')
    m = input('请输入月份')
    d = input('请输入日')
    lis = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日',]
    dic = dict(enumerate(lis))
    if y.isdigit() and m.isdigit() and d.isdigit() and 1<=int(m)<=12 and 1<=int(d)<=31 :
        w = calendar.weekday(int(y),int(m),int(d))
        print(dic[w])
# print(what_the_day())

def reverse_string(str):
    if str == "":
        return str
    else:
        return reverse_string(str[1:])+str[0]
print(reverse_string("abcdef"))
