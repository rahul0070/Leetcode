class Solution:
	def hasPathSum(self, node, x):
		if not node:
			return False
		x -= node.val

		if x == 0:
			if not node.right and not node.left:
				return True
		return self.hasPathSum(node.left, x) or self.hasPathSum(node.right, x)

	def pathSum(self, node, x):
		self.res = []
		self.run(node, x, [])
		return self.res

	def run(self, node, x, path):
		if node:
			x -= node.val
			p = path + [node.val]
			
			if x == 0:
				if not node.right and not node.left:
					self.res.append(p)

			self.run(node.left, x, p)
			self.run(node.right, x, p)
