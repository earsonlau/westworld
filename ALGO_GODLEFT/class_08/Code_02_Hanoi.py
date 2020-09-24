#汉诺塔问题
class Solution:
    def hanoi(self,n):
        if n > 0:
            self.func(n, n, "left","mid","right")
    def func(self,rest,down,from_,help,to):
        #参数解释：
        # rest 是本次调用func需要执行搬运的盘子数(继续往下递归的次数-1)，若rest为1，则打印本次搬运的盘子id和起始位置终止位置
        # down 是本次搬运的盘子id
        # from 是起始位置
        # help 是中间位置
        # to 是终止位置
        if rest == 1 :
            print("move ",down,"from ",from_, "to", to )
        else:
            #三步走
            #1. 把n-1个盘子放到mid上面
            self.func(rest - 1,down - 1 ,from_,to,help)
            #2. 把第n个盘子放到right上面
            self.func(1,down,from_,help,to)
            #3. 把mid上面的n-1个盘子放到right上面
            self.func(rest - 1,down - 1,help,from_,to)

sol = Solution()
sol.hanoi(3)