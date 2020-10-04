# 给定一个整型数组arr，代表数值不同的纸牌排成一条线，
# 玩家A和玩家B依次拿走每张纸牌
# 规定玩家A先拿玩家B后拿
# 但是每个玩家每次只能拿走最左或最右的纸牌，
# 玩家A和玩家B都绝顶聪明。请返回最后获胜者的分数

def win1(arr):
    if len(arr) == 0:
        return 0
    #先手和后手返回分数多的
    return max(f(arr,0,len(arr) - 1), s(arr,0,len(arr) - 1))
def f(arr,L,R):
    if L == R:
        return arr[L]
    #因为是先手，分为拿了最左边的牌arr[L]和拿最右边的牌arr[R]两种情况
    #留给自己最好的结果(max)
    return max(arr[L] + s(arr,L+1,R)
               ,
               arr[R] + s(arr,L,R-1))

def s(arr,i,j):
    if i == j:
        #就一张牌了，我还要等对方先拿，那我没得拿了直接返回0
        return 0
    #因为对手很鸡贼，所以他一定会留给我比较差的结果(min)
    return min (f(arr,i+1,j),#对手拿走了arr[i]
                f(arr,i,j-1)#对手拿走了arr[j]
                )