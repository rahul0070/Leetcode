from collections import deque
import copy

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxLevelSum(self, root):
		#BFS
		if root == None:
			return 0

		result = root.val
		resIndex = 1
		queue = deque()
		queue.append(root)
		lvl = 0

		while queue:
			lvl += 1
			row = 0
			iterator = []
			for q in queue:
				iterator.append(q)

			for n in iterator:
				row += n.val
				if n.left != None:
					queue.append(n.left)

				if n.right != None:
					queue.append(n.right)
				queue.popleft()

			if result < row:
				result = row
				resIndex = lvl
		return resIndex


	def traverse(self, root, rec):
		# DFS
		if root != None:
			if rec not in self.resDict:
				self.resDict[rec] = 0

			self.resDict[rec] += root.val
			self.traverse(root.left, rec+1)
			self.traverse(root.right, rec+1)

	def maxLevelSum(self, node):
		#DFS
		self.resDict = {}
		self.traverse(node, 0)
		print(self.resDict)
		return 1 + max(self.resDict, key=lambda key: self.resDict[key])


if __name__ == '__main__':
	s = Solution()
	Tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7)))
	Tree2 = TreeNode(1, TreeNode(12, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2, None, None))
	print(s.maxLevelSum(Tree2))