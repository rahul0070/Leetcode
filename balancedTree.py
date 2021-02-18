
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def __init__(self):
		self.ht = {}

	def height(self, node):
		if node == None:
			return 0
		elif node in self.ht:
			return self.ht[node]
		else:
			result = 1 + max(self.height(node.right), self.height(node.left))
			self.ht[node] = result
			return result

	def isBalanced(self, node):
		if node != None:
			if abs(self.height(node.right)-self.height(node.left)) > 1:
				self.res = False
				return False
			else:
				return self.isBalanced(node.left) and self.isBalanced(node.right)
		else: return True


if __name__ == '__main__':
	s = Solution()
	Tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7)))
	Tree2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2, None, None))
	sub = TreeNode(3, TreeNode(4), TreeNode(4)
	print(s.isBalanced(Tree))