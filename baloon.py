class Solution:
	def __init__(self):
		self.result = 0

	def getCost(self, index, baloons):
		if index == len(baloons)-1:
			return baloons[index-1]

		elif index == 0:
			return baloons[index+1]

		else:
			return baloons[index-1]*baloons[index+1]

	def maxCoins(self, baloons):
		print(baloons)
		if baloons == []:
			return self.result

		elif len(baloons) == 1:
			return self.result + baloons[0]

		max = baloons[0]
		maxValue = baloons[0]
		maxIndex = 0
		for i in range(len(baloons)):
			p = self.getCost(i, baloons)
			if p > max:
				max = p
				maxValue = baloons[i]
				maxIndex = i

		sol = maxValue * max
		self.result += sol
		print(maxValue, sol)
		baloons.remove(maxValue)
		return self.maxCoins(baloons)


s = Solution()
print(s.maxCoins([9,76,64,21,97,60,5]))