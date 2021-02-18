class Solution:
	def climbStairs(self, n):
		if n == 1: 
			return 1
		elif n == 2: 
			return 3
		else: 
			return 2 + climbStairs(n-1) + climbStairs(n-2)

	def climbStairs(self, n):
		table = [1, 1, 2]
		result = 0
		if n <= 2:
			return table[n]
			
		for i in range(3, n):
			table.append(table[i-1] + table[i-2])

		return table[-1]

if __name__ == '__main__':
	print(s(5)) 