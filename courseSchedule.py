class Solution:

	def isCompleted(self, id):
		return self.completed[id]

	def canFinish(self, n, co):
		self.pre = {}
		self.completed = {}

		for i in co:
			if i[0] not in self.pre:
				self.pre[i[0]] = [i[1]]
				self.completed[i[0]] = False
				self.completed[i[1]] = False
			else:
				self.pre[i[0]].append(i[1])
				self.completed[i[1]] = False

		for k, v in self.pre.items():
			if self.completed[k] == False:
				for i in v:
					d = self.new()
					if self.complete(i, d) == False:
						return False
		return True

	def complete(self, id, visited):
		if visited[id] == True:
			return False
		else: visited[id] = True

		if id in self.pre:
			for i in self.pre[id]:

				if not self.completed[i]:
					if not self.complete(i, visited):
						return False

			self.completed[id] = True
			return True
		else:
			self.completed[id] = True
			return True

	def loop(self, id1, id2):
		if id2 in self.pre:
			li = self.pre[id2]
			for i in li:
				if i == id1:
					return True
		return False

	def new(self):
		dict = {}
		for i,j in self.completed.items():
			dict[i] = False
		return dict


s = Solution()
print(s.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))