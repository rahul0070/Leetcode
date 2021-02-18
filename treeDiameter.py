
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def height(self, node):
		if node == None:
			return 0
		elif node in self.ht:
			return self.ht[node]
		else:
			result = max(self.height(node.right)+1, self.height(node.left)+1)
			self.ht[node] = result
			return result

	def run(self, node):
		if node == None:
			return 

		h1 = self.height(node.right)
		h2 = self.height(node.left)
		h = h1+h2

		if h > self.res:
			self.res = h

		if max(h1,h2)*2 < self.res:
			return

		if h1 > h2:
			self.run(node.right)
		else:
			self.run(node.left)

	def diameterOfBinaryTree(self, node):
		self.ht = {}
		self.res = 0
		self.run(node)
		return self.res


if __name__ == '__main__':
	s = Solution()
	Tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(s.diameterOfBinaryTree(Tree))