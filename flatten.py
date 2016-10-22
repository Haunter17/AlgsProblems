class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
     #    if root is None or root.left is None:
     #    	return
     #    tmp = root.right
     #    if root.left is not None:
     #    	self.flatten(root.left)
     #    	root.right = root.left
     #    	root.left = None
     #    while root.right is not None:
     #    	root = root.right
     #    self.flatten(tmp)
    	# root.right = tmp
    	if root is None:
    		return
    	self.flatten(root.left)
    	self.flatten(root.right)
    	if root.left is None:
    		return
    	tmp = root.left
    	while tmp.right:
    		tmp = tmp.right
    	tmp.right = root.right
    	root.right = root.left
    	root.left = None


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node5
node2.left = node3
node2.right = node4
node5.right = node6

soln = Solution()
soln.flatten(node1)

# print node5.val
# print node5.right.val
root = node1
while root is not None:
	print root.val
	root = root.right
