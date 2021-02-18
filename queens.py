class Solution:
	def __init__(self):
		self.results = []

	def solveNQueens(self, n):
		self.n = n
		self.track(0, [])
		return self.getResult(self.results)

	def make(self, n):
		res = []
		for i in range(n):
			res.append('.')
		return res

	def canAttack(self, row, colIndex, sol):
		for i in range(len(sol)):
			if colIndex == sol[i]:
				return True
			elif abs(colIndex-sol[i]) == abs(row-i):
				return True
		return False


	def getPossible(self, sol, row):
		res = []
		for i in range(self.n):
			if self.canAttack(row, i, sol) != True:
					res.append(i)
		return res

	def track(self, x, sol):
		if sol == []:
			for i in range(self.n):
				self.track(x+1, [i])

		elif x == self.n:
			self.results.append(sol)

		else:
			li = self.getPossible(sol, x)
			for i in li:
				self.track(x+1, sol + [i])

	def convert(self, solution):
		result = []
		for i in range(len(solution)):
			res = self.make(self.n)
			res[solution[i]] = 'Q'
			result.append(''.join(res))
		return result

	def getResult(self, output):
		result = []
		for i in output:
			result.append(self.convert(i))
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.solveNQueens(5))