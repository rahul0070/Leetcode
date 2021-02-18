class Solution:
	def wordBreak(self, s, data):
		self.string = s
		self.words = {}
		self.n = len(s)
		self.f = {}
		for i in data:
			self.words[i] = 1

		for i in reversed(range(self.n+1)):
			self.f[i] = self.run(i)

		return self.f[0]

	def run(self, i):
		if i in self.f:
			return self.f[i]

		if i >= self.n:
			return True

		ind = i
		while ind <= self.n:
			if self.string[i:ind] in self.words:

				if ind in self.f:
					res = self.f[ind]
				else:
					res = self.run(ind+1)
				if res:
					return True
			
			ind += 1

		return False