class Solution:
	def wordBreak(self, s, data):
		self.string = s
		self.words = {}
		self.n = len(s)
		self.f = {}
		for i in data:
			self.words[i] = 1

		self.f[self.n] = True
		for i in reversed(range(self.n)):
			self.f[i] = self.run(i)

		return self.f[0]

	def run(self, i):
		ind = i
		while ind <= self.n:
			if self.string[i:ind] in self.words:
				res = self.f[ind]
				if res:
					return True
			ind += 1
		return False


s = Solution()
#print(s.wordBreak("leetcode", ["leet","code"]))
print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))