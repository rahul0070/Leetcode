class Node:
	def __init__(self, i, j):
		self.val = (i,j)
		self.children = []

class Solution:
	parse = []
	def createTree(self, grid):
		for i in range(len(grid)):
			row = []
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					if row[]
					row.append(1)
					Node(i,j)
				else:
					row.append(0)

	def orangesRotting(self, grid):
		self.createTree(grid)


if __name__ == '__main__':
	s = Solution()
	li = [[2,1,1],[1,1,0],[0,1,1]]
	print(s.orangesRotting(li))