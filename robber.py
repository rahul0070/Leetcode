class Solution:
	def rob(self, li):
		if li == []:
			return 0

		n = len(li)
		if n == 1:
			return li[0]

		result = []
		result.append(li[0])
		result.append(max(result[0], li[1]))

		for i in range(2, n):
			result.append(max(li[i] + result[i-2], result[i-1]))

		return result[-1]

	def rob(self, li):
		if li == []:
			return 0

		n = len(li)
		if n == 1:
			return li[0]

		p1 = li[0]
		p2 = max(p1, li[1])

		for i in range(2, n):
			curr = max(li[i] + p1, p2)
			p1 = p2
			p2 = curr

		return p2	