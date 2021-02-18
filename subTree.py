
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isEquals(self, root1, root2):
		if root1 == None or root2 == None:
			return (root1 == None) and (root2 == None)

		elif root1.val == root2.val:
			return self.isEquals(root1.right, root2.right) and self.isEquals(root1.left, root2.left)

		else: return False

	def isSubtree(self, node, sub):
		if node != None:
			if self.isEquals(node, sub):
					return True
			else:
				return self.isSubtree(node.left, sub) or self.isSubtree(node.right, sub)
		else: return self.isEquals(node, sub)


if __name__ == '__main__':
	s = Solution()
	Tree2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2, None, None))
	sub = TreeNode(3, TreeNode(4), TreeNode(4)
	print(s.isSubtree(Tree2, sub))