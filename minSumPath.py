class Solution:
	def minPathSum(self, grid):
		prev = [grid[0][0]]
		for i in range(1, len(grid[0])):
			prev.append(prev[i-1]+grid[0][i])

		row = []
		for i in range(1, len(grid)):
			for j in range(len(grid[0])):
				current = grid[i][j]
				if j == 0:
					row.append(current + prev[0])
				else:
					row.append(min(prev[j], row[j-1]) + current)
			prev = row
			row = []

		return prev[-1]