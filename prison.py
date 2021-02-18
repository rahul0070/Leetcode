import copy
class Solution:
	def __init__(self):
		self.previous = []

	def adjacentIsEqual(self, index):
		if index == 0 or index == 7:
			return False
		elif self.previous[index-1] == self.previous[index+1]:
			return True
		else:
			return False

	def update(self):
		for i in range(len(self.cells)):
			if self.adjacentIsEqual(i):
				self.cells[i] = 1
			else:
				self.cells[i] = 0


	def prisonAfterNDays(self, cells, n):
		if n > 15:
			n = (n%15)+1
			if n > 7:
				n = (15 - n) + 1
		self.cells = cells
		for i in range(1, n+1):
			if i == 15:
				print('-------\n')
			
			self.previous = copy.deepcopy(self.cells)
			self.update()
			print(i, self.cells)
		return self.cells


s = Solution()
li = [0,1,0,1,1,0,0,1]
li2 = [1,0,0,1,0,0,1,0]
print('Ans: ', s.prisonAfterNDays(li2, 10)) #15

#[0, 1, 1, 1, 0, 0, 1, 0]