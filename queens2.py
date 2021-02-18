class Solution:
	def totalNQueens(self, n):
		self.results = 0
		self.n = n
		self.track(0, [])
		return self.results

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

		elif x == self.n: self.results += 1

		else:
			for i in self.getPossible(sol, x):
				self.track(x+1, sol + [i])

if __name__ == '__main__':
	s = Solution()
	print(s.solveNQueens(5))