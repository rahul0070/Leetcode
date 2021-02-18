class Solution:
	def stoneGame(self, piles):
		self.a = piles
		self.alex = 0
		self.lee = 0
		score, index = self.f(0, len(piles)-1)
		leeScore = sum(piles) - score
		if score > leeScore:
			return True
		else:
			return False

	def f1(self, i, j):
		if i == j or i > j:
			return 0, 1

		s1, i1 = self.f1(i+1, j)
		s2, i2 = self.f1(i, j-1)

		if s1 > s2:
			self.lee += s1
			oIndex = i1
		else:
			self.lee += s2
			oIndex = i2


		if oIndex == 1:
			ss1, ii1 = self.f1(i+2, j)
			ss2, ii2 = self.f1(i+1, j-1)
			
			if ss1 + self.a[i] > ss2 + self.a[j]:
				score = ss1 + self.a[i]
				index = 1
			else:
				score = ss2 + self.a[j]
				index = 2

		elif oIndex == 2:
			ss1, ii1 = self.f1(i+1, j-1)
			ss2, ii2 = self.f1(i, j-2)
			
			if ss1 + self.a[i] > ss2 + self.a[j]:
				score = ss1 + self.a[i]
				index = 1
			else:
				score = ss2 + self.a[j]
				index = 2

		return score, index

	def f(self, i, j):
		if i == j or i > j:
			return 0, 1

		s1, i1 = self.f1(i+1, j)
		s2, i2 = self.f1(i, j-1)

		if s1 > s2:
			oIndex = i1
		else:
			oIndex = i2

		if oIndex == 1:
			r1 = self.f(i+2, j) + self.a[i]
			r2 = self.f(i+1, j-1) + self.a[j]
			return max(r1, r2)

		elif oIndex == 2:
			r1 = self.f(i+1, j-1) + self.a[i]
			r2 = self.f(i, j-2) + self.a[j]
			return max(r1, r2)


s = Solution()
print(s.stoneGame([5,3,4,5]))