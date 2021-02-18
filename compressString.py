class Solution:
	def compress(self, li):
		if li == []:
			return ''

		result = [li[0]]
		s = li[0]
		count = 1

		for i in li:
			iterator.append(i)

		for i in range(1, len(iterator)):
			if iterator[i] != s:
				if count != 1:
					result.append(str(count))
				count = 1
				s = iterator[i]
				result.append(s)

			else:
				li.remove(li[i])
				count += 1

		result.append(str(count))
		return result

