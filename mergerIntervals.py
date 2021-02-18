class Solution:
	def merge(self, li):
		li.sort()
		s = li[0][0]
		e = li[0][1]
		result = []
		for i in range(1, len(li)):
			if li[i][0] <= e:
				if li[i][1] > e:
					e = li[i][1]
			else:
				result.append([s, e])
				s = li[i][0]
				e = li[i][1]
		result.append([s, e])
		return result
		
if __name__ == '__main__':
	s = Solution()
	li = [[1,3],[2,6],[8,10],[15,18]]
	print(s.merge(li))