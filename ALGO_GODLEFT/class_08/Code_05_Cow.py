#假设农场中成熟的母牛每年只会生1头小母牛，并且永远不会死。第一年农场有1只成熟的母牛，
# 从第二年开始，母牛开始生小母牛。每只小母牛3年之后成熟又可以生小母牛。给定整数N，求
# 出N年后牛的数量。
class Code_05_Cow():
    def cow(self,n):
        if n < 1 :
            return 0
        if n == 1 or n == 2 or n == 3:
            return n
        return self.cow(n-1)+self.cow(n-3)
print(Code_05_Cow().cow(3))