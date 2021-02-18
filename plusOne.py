class Solution:
	def plusOne(self,li):
		res = []
		toAdd = 1
		for i in reversed(range(len(li))):
			if toAdd == 1:
				add = li[i] + 1
				if add > 9:
					res.append(0)


if __name__ == '__main__':
	s = Solution()
	li = [4,3,2,1]
	print(s.run(li))