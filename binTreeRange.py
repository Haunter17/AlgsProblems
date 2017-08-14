class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
	def __init(self):
		self.answer = None
		self.maxTreeSize = 0
	def findMaxTreeInRange(self, root, lower, upper):
		pass

	def findHelper(self, root, lower, upper):
		if root is None:
			return (0, False)

		if root.left is None and root.right is None:
			if root.val < lower or root.val > upper:
				return (0, False)
			return (1, True)

		leftMax, rightMax = (0, True), (0, True)
		if root.left is not None:
			leftMax = self.findHelper(root.left, lower, upper)
		if root.right is not None:
			rightMax = self.findHelper(root.right, lower, upper)

		if root.val >= lower and root.val <= upper:
			if leftMax[1] and rightMax[1]:
				return (1 + leftMax[0] + rightMax[0], True)
			else:
				return (max(leftMax[0], rightMax[0]), False)
		else:
			return (max(leftMax[0], rightMax[0]), False)

node0 = TreeNode(25)
node1 = TreeNode(19)
node2 = TreeNode(37)
node3 = TreeNode(12)
node4 = TreeNode(22)
node5 = TreeNode(29)
node6 = TreeNode(4)
node7 = TreeNode(23)
node8 = TreeNode(30)

node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node3.left = node6
node4.right = node7
node5.right = node8

print Solution().findHelper(node0, 1, 100)
