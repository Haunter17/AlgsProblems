
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        res = []
        self.processLevel(root, 0, res)
        return res
    
    def processLevel(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.processLevel(root.left, level + 1, res)
            self.processLevel(root.right, level + 1, res)

    def processLevelReverse(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[len(res) - 1 - level].append(root.val)
            self.processLevel(root.left, level + 1, res)
            self.processLevel(root.right, level + 1, res)
