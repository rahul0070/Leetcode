def smallestSubArrayWithGivenSum(x, li):
	if len(li) == 0:
		return -1

	p1 = 0
	p2 = 0
	s = li[0]
	n = len(li)
	res = 0

	while p1 < n or p2 < n:
		print(p1, p2, res)
		if s == x:
			ch = (p2-p1)+1
			if ch < res:
				res = ch
			s -= li[p1]
			s += li[p2]
			p1 += 1
			p2 += 1

		elif s > x:
			s -= li[p1]
			p1 += 1
			ch = (p2-p1) + 1
			if ch < res or res == 0:
				res = ch

		elif s < x:
			s += li[p2]
			p2 += 1
			ch = res
	return res

def longestSubString(str, k):
	p1 = 0
	p2 = 0
	n = len(li)
	res = 0
	data = {}
	count = 0

	while p1 < n or p2 < n:
		if count > k:
			data[str[p1]] = 0
			p1 += 1

		if p1 == 0 and p2 == 0:
			data[str[p1]] = 1
			p2 += 1
			flag = 2
			count += 1
		
		elif flag == 2:
			if str[p2] in data:
				if data[str[p2]] == 1:
					p2 += 1
				else:
					count += 1
			else:
				count += 1





print(smallestSubArrayWithGivenSum(7, [2,1,5,2,8]))