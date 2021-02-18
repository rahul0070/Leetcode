class Solution:
	def uniquePaths(self, m, n):
		prev = []
		for i in range(m):
			row = []
			for j in range(n):
				if i == 0 or j == 0: row.append(1)
				else: row.append(row[j-1] + prev[j])
			prev = row

		prev = []
		return row[-1]


if __name__ == '__main__':
	s = Solution()
	m = 3
	n = 7
	print(s.uniquePaths(m, n))