class Solution:
	def __init__(self):
		self.result = 0
		self.data = {}

	def maxCoins(self, li):
		return self.run(li)

	def run(self, li):
		# #print('C: ', li)
		# t = tuple(li)
		# if t in self.data:
		# 	print('w')
		# 	return self.data[t]

		res = []
		n = len(li)
		if n == 1:
			res = [li[0]]
		else:
			for i in range(n):
				#print('f ', li)
				if i == 0:
					x = li[i] * li[i+1]
				elif i == n-1:
					x = li[i] * li[i-1]
				else:
					x = li[i] * li[i+1] * li[i-1]
				res.append(x + self.run(li[:i] + li[i+1:]))

		result = max(res)
		#print(li, result, res)
		# self.data[t] = result
		return result

s = Solution()
print(s.maxCoins([3,1,5,8]))