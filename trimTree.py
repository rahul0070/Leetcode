
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:

	def trimBST(self, node, low, high):
		if node != None:
			if node.val < low or node.val > high:
				if node.right != None:
					node = node.right
				elif node.left != None:
					node = node.left
				else:
					node = None

			if node != None:
				node.left = self.trimBST(node.left, low, high)
				node.right = self.trimBST(node.right, low, high)
				return node
			else:
				return None
		else:
			return None

if __name__ == '__main__':
	def printT(node):
		if node != None:
			print(node.val)
			printT(node.left)
			printT(node.right)

	s = Solution()
	#Tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7)))
	#Tree2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2, None, None))
	Tree3 = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1), None)), TreeNode(4, None, None))
	t = TreeNode(1, TreeNode(0), TreeNode(2))
	printT(s.trimBST(t, 1, 2))