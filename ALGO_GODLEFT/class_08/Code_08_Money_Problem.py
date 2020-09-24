class Code_08_Money_Problem :
	def money1(self,arr, aim):
		return self.process1(arr, 0, 0, aim)

	def process1(self,arr, i, sum, aim):
		if sum == aim:
			return True
		# sum != aim
		if i == len(arr):
			return False
		return self.process1(arr, i + 1, sum, aim) or self.process1(arr, i + 1, sum + arr[i], aim)

sol = Code_08_Money_Problem()
print(sol.money1([2,3,5],7))