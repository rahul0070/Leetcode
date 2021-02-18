class Solution:
	def minHeightShelves(self, li, w):
		books = sorted(li, key=lambda x: x[1])

		result = 0
		row = 0
		for i in books:
			


s = Solution()
print(s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))