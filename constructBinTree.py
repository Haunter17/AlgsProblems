class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        return self.buildHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def buildHelper(self, preorder, pStart, pEnd, inorder, iStart, iEnd):
        if pStart > pEnd or iStart > iEnd:
            return
        curr = preorder[pStart]
        posIn = inorder.indexOf(curr)
        root = TreeNode(curr)
        root.left = self.buildHelper(preorder, pStart + 1, posIn - iStart + pStart ,inorder, iStart, posIn - 1)
        root.right = self.buildHelper(preorder,posIn - iStart + pStart + 1 ,pEnd,inorder, posIn + 1, iEnd)

        return root
