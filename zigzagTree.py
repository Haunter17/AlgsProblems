import copy
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        if root is None:
            return res
        stack1 = []
        stack2 = []
        stack1.append(root)

        while len(stack1) > 0 or len(stack2) > 0:
            currLevel = []
            while len(stack1) > 0:
                node = stack1.pop()
                currLevel.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                if len(stack1) == 0:
                    tmp = copy.deepcopy(currLevel)
                    res.append(tmp)

            currLevel = []
            while len(stack2) > 0:
                node = stack2.pop()
                currLevel.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
                if len(stack2) == 0:                    
                    tmp = copy.deepcopy(currLevel)
                    res.append(tmp)
        return res

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

soln = Solution()
print soln.zigzagLevelOrder(node1)
         