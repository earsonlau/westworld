#斐波那契数列
class Code_01_Factorial:
    def get_factorial1(self,n):
        if n == 1 :
            return 1
        else :
            return n * self.get_factorial1(n-1)

    def get_factorial2(self,n):
        res = 1
        for i in range(1,n+1):
            res *= i
        return res
sol = Code_01_Factorial()
print(sol.get_factorial1(3))
print(sol.get_factorial2(3))