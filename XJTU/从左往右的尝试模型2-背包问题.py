#给定两个长度都为N的数组 weights values
#weights[i]和values[i]分别代表i号物品的重量和价值(all >0)
#给一个正数bag，表示一个载重为bag的袋子
#你装的物品不能超过载重，问能装下的最大价值
w = [2,4,7]
v = [6,3,19]

def bag1(w,v,bag_):
    return process(w,v,0,0,bag_)

#尝试1
#不变的变量： w,v,bag
#轮到第index个货物
#0...index-1号货物挑选后背包目前负载为alreadyW
#如果返回-1 表示没有方案
#如果不返回-1 则认为返回的东西是真实的价值
# def process(w,v,index,alreadyW,bag):
#     if alreadyW > bag:
#         #背包已满，本次选择无效
#         return -1
#     #重量没超
#     if index == len(w):
#         #已经放满了，不能再放了，所以index之后的价值为0
#         return 0
#     #p1表示我没有拿第index号货物
#     p1 = process(w,v,index+1,alreadyW,bag)
#     #p2next表示我拿了第index号货物
#     p2next = process(w,v,index+1,alreadyW+w[index],bag)
#     p2 = -1
#     if p2next != -1 :
#         #当前货物价值v[index]+后续货物价值p2next为拿了第index号货物的总价值
#         p2 = v[index]+ p2next
#     #返回拿/不拿第index号货物的最大价值
#     return max(p1,p2)


def bag2(w,v,bag_):
    return process(w,v,0,bag_)
#尝试2
#只剩下rest的空间了
#index...货物自由选择，但是剩余空间不要小于0
#返回能够获得的最大价值
def process(w,v,index,rest):
    if rest < 0 :
        return -1 #无效方案
    # rest >= 0:
    if index == len(w):
        return 0
    #有货也有空间
    #不要index号货物所产生的价值记为p1
    p1 = process(w,v,index+1,rest)
    #要index号货物所产生的价值记为p2
    p2 = -1
    p2next = process(w,v,index+1,rest-w[index])
    if p2next != -1:
        p2 = v[index] + p2next
    return max(p1,p2)


def dpway(w,v,bag_):
    N = len(w)
    dp = [[0 for i in range(bag_+1)] for j in range(N+1)]
    for index in range(N-1, -1, -1):
        for rest in range(0, bag_+1):
            # 有货也有空间
            # 不要index号货物所产生的价值记为p1
            p1 = dp[index + 1][rest]
            # 要index号货物所产生的价值记为p2
            p2 = -1
            if rest - w[index] >= 0:
                p2 = v[index] + dp[index+1][rest - w[index]]
            dp[index][rest] = max(p1, p2)
    return dp[0][bag_]

print(bag2(w,v,12))
print(dpway(w,v,12))