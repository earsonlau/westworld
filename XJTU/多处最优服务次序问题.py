# 西交2017真题
#  题目描述：
# ¢ 设有n个顾客同时等待一项服务，顾客i需要的服务时间为Ti，1≤i≤n，
# 共有s处可以提供此项服务。应如何安排n个顾客的服务次序才能使平均等待时间达到最小？
# 平均等待时间是n个顾客等待服务时间的总和除以n。
# ¢ 给定的n个顾客需要的服务时间和s的值，编程计算最优服务次序。
#
# ¢ 输入
# 第一行有2个正整数n和s，表示有n个顾客且有s处可以提供顾客需要的服务。
# 接下来的1行中，有n个正整数，表示n个顾客需要的服务时间。
#
# ¢ 输出
# 最小平均等待时间，输出保留3位小数。
#
#  输入样例
# 10 2
# 56 12 1 99 1000 234 33 55 99 812
#
# 输出样例

# int service[SIZE];  # Storage service point
# int time_sum[SIZE];  # Storage service waiting time
# problem analysis:
#
# 每个顾客需要被服务的时长A[n] = {56,12,1,99,1000,234,33,55,99,812}
# 每个顾客按照自己需要被服务的时长排序后被分配到两个窗口接受服务
#                 /  service[0]   1    33   56   99    812
# S service points
#                 \  service[1]  12   55   99  234  1000
#
# service[index]只存放第index号窗口总共服务了多久
# time_sum[index]只存放第index号窗口被顾客等待的总时长
# service[0] = A[0]       time_sum[0] = service[0] = A[0]
# 第0号顾客被服务结束后，service[0]累计服务了0号顾客的时长，time_sum[0]存放第0号顾客的等待时长
# service[1] = A[1]       time_sum[1] = service[1] = A[1]
# 第1号顾客被服务结束后，service[1]累计服务了1号顾客的时长，time_sum[1]存放第1号顾客的等待时长
# service[0] = A[0] + A[2]      time_sum[0] = 2 A[0] + A[2]
# service[1] = A[1] + A[3]      time_sum[1] = 2A[1] + A[3]
#
# 第2号顾客被服务结束后，service[0]累计服务了0号和2号顾客的时长，time_sum[0]存放第0号和2号顾客的等待时长
# 第3号顾客被服务结束后，service[1]累计服务了1号和3号顾客的时长，time_sum[1]存放第1号和3号顾客的等待时长
# servicey analogy, the principle is like the optimal service order.
# time_sum[0] = 5A[0] + 4 A[2] + 3A[4] +2 A[6] + A[8]
# time_sum[1] = 5A[1] + 4 A[3] + 3A[5] +2 A[7] + A[9]
# 第8号顾客被服务结束后，service[0]累计服务了0.2.4.6.8号顾客的时长，time_sum[0]存放第0.2.4.6.8号顾客的等待时长
# 第9号顾客被服务结束后，service[1]累计服务了1.3.5.7.9号顾客的时长，time_sum[1]存放第1.3.5.7.9号顾客的等待时长
def service_order(n,s,t):
    time_sort = sorted(t)# 所有的服务时间先排个序
    print("Minimum average waiting time:", greedy(time_sort,s))

def greedy(A,s):
    print("排序后的顾客服务时间",A)
    i = 0
    j = 0
    service = [0 for i in range(s)] # 服务点每个顾客的等待时间
    time_sum = [0 for i in range(s)] # 服务点顾客等待的时间总和
    while (i < len(A)):
        service[j] += A[i]
        time_sum[j] += service[j]
        i += 1
        j = (j+1) % s   # Arrange the activities of s service points

    t = 0
    for i in range(s):
        t += time_sum[i]  # 计算所有服务点服务时间总和
    return t / len(A)

n = 10
s = 2
t = [56,12,1,99,1000,234,33,55,99,812]
service_order(n,s,t)