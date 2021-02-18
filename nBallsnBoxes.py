class Solution:
	def find(self, box, balls):
		if box > balls:
			return []
		else:
			#balls = 15; box = 10
			n = balls-box
			self.balls = balls
			self.data = {}
			self.box = box
			self.result = []
			self.run(0, n, box, [], {})
			return self.result

	def run(self, b1, b2, box, sol):
		if len(sol) == self.box:
			for i in range(len(sol)):
				sol[i] += 1
			if sum(sol) == self.balls:

				self.result.append(sol)

		elif b2 == 0:
			self.run(b1, 0, box-1, sol + [0])


		else:
			for i in range(b1, b2+1):
				self.run(i, b2 - i, box - 1, sol + [i])




s = Solution()
print(s.find(3, 9))
