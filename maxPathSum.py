class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
    	self.maxPath = -float('inf')

    def maxPathSum(self, root):
        # write your code here
        self.opt(root)
        return self.maxPath

    def opt(self, node):
    	if node is None:
    		return 0
    	leftPathSum = self.opt(node.left)
    	rightPathSum = self.opt(node.right)

    	maxSingle = max(max(leftPathSum, rightPathSum) + node.val, node.val)
    	maxOpt = max(leftPathSum + rightPathSum + node.val, maxSingle)
    	
    	self.maxPath = max(self.maxPath, maxOpt)

    	return maxSingle

# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)

# node1.left = node2
# node1.right = node3
root = TreeNode(10)
root.left = TreeNode(2)
root.right   = TreeNode(10);
root.left.left  = TreeNode(20);
root.left.right = TreeNode(1);
root.right.right = TreeNode(-25);
root.right.right.left   = TreeNode(3);
root.right.right.right  = TreeNode(4);

soln = Solution()
print soln.maxPathSum(root)