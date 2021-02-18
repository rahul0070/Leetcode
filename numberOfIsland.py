
class Solution:
	def getNeighbors(self, r, c):
		res = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
		for i in res:
			r = i[0]
			c = i[1]
			if r > len(self.grid)-1 or r < 0 or c > len(self.grid[0])-1 or c < 0:
				res.remove(i)
		return res


	def isNeighbor(self, a1, a2, b1, b2):
		neigh = self.getNeighbors(b1, b2)
		for i in neigh:
			if i == [a1, a2]:
				return True
		return False

	def rearrange(self, data):
		val = list(data.values())
		result = {}
		for i in range(len(val)):
			result[i] = val[i]

		return result


	def isInIsland(self, r, c):
		if self.islands == {}:
			self.islands[0] = [[r, c]]
		else:
			self.islands = self.rearrange(self.islands)
			flag = 0
			counter = 0
			while counter in self.islands:
				value = self.islands[counter]
				for i in value:
					if self.isNeighbor(r, c, i[0], i[1]):
						if flag == 0:
							value.append([r, c])
							self.f2 = [r, c+1]
							master = counter
							flag = 1
							break
						else:
							for j in value:
								self.islands[master].append(j)
							self.islands.pop(counter)
				counter += 1

			if flag == 0:
				self.islands[counter+1] = [[r, c]]


	def numIslands(self, grid):
		self.islands = {}
		self.grid = grid
		self.f2 = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if int(grid[i][j]) == 1:
					self.isInIsland(i, j)

		return len(self.islands)


s = Solution()
g = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
g2 = [["1","1","1","1","0"],["1","0","0","0","0"],["1","0","1","0","0"],["1","1","1","1","0"]]

g1 = [["1","1","1","1","1","1","1","1","1"],
 ["1","0","0","0","0","0","0","0","1"],
 ["1","0","1","0","1","0","1","0","1"],
 ["1","0","1","1","1","1","1","0","1"],
 ["1","0","1","0","1","0","1","0","1"],
 ["1","0","0","0","0","0","0","0","1"],
 ["1","1","1","1","1","1","1","1","1"]]

# g4 = [["1","1","1","1","1","1","1"],
#   ["1","0","0","0","0","0","1"],
#   ["1","0","1","0","1","0","1"],
#   ["1","0","1","1","1","0","1"],
#   ["1","0","1","0","1","0","1"],
#   ["1","0","0","0","0","0","1"],
#   ["1","1","1","1","1","1","1"]]

print(s.numIslands(g1))

