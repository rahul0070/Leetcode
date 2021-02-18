class Solution:
	def reorganizeString(self, st):
		self.data = {}
		for i in st:
			if i not in self.data:
				self.data[i] = 1
			else:
				self.data[i] += 1

		m = max(self.data)
		mv = self.data[m]

		self.data[m] = 0

		total = 0
		for k, v in self.data.items():
			total += v

		print(total, mv)