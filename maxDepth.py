class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxDepth(self, node):
		if node != None: return 1 + max(self.maxDepth(node.right), self.maxDepth(node.left))
		else: return 0

	def minDepth(self, node):
		if node != None: 
			l = self.minDepth(node.left)
			r = self.minDepth(node.right)
			if r!=0 and l == 0: return r+1
			elif l!=0 and r == 0: return l+1
			else: return (min(l,r) + 1)
		else: return 0


s = Solution()
t = TreeNode(1, None, TreeNode(2, None, TreeNode(7)))
print(s.minDepth(t))