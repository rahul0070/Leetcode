class Solution:
	def uniquePathsWithObstacles(self, grid):
		prev = []
		for i in range(len(grid)):
			row = []
			for j in range(len(grid[0])):
				if i == 0 and j == 0: 
					if grid[i][j] == 1:
						return 0
					else:
						row.append(1)

				elif grid[i][j] == 1: row.append(0)

				elif i == 0:
					if row[j-1] != 0: 
						row.append(1)
					else:
						row.append(0)

				elif j == 0:
					if prev[0] != 0: 
						row.append(1)
					else:
						row.append(0)

				else: row.append(row[j-1] + prev[j])

			prev = row
		prev = []
		return row[-1]


if __name__ == '__main__':
	s = Solution()
	m = 3
	n = 7
	g = [[0,1],[0,0]]
	grid = [[0,0,0],[0,1,0],[0,0,0]]
	g2 = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	print(s.uniquePathsWithObstacles(g2))