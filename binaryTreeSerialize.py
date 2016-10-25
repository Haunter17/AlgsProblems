
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        queue = []
        queue.append(root)

        index = 0
        while index < len(queue):
            curr= queue[index]
            if curr is not None:
                queue.append(curr.left)
                queue.append(curr.right)
            index += 1
        return ','.join([str(node.val) if node else '#' for node in queue])

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        data = data.strip('\n')
        val = data.split(',')
        nodes = [None for x in range(len(val))]
        hashCount = 0

        for i in range(len(val)):
            if val[i] != '#':
                if nodes[i] is None:
                    nodes[i] = TreeNode(int(val[i]))
                left = 2 * (i - hashCount) + 1
                right = 2 * (i - hashCount) + 2
                # print i, hashCount, left, right
                if val[left] != '#':
                    if nodes[left] is None:
                        nodes[left] = TreeNode(int(val[left]))
                    nodes[i].left = nodes[left]
                if val[right] != '#':
                    if nodes[right] is None:
                        nodes[right] = TreeNode(int(val[right]))
                    nodes[i].right = nodes[right]
            else:
                hashCount += 1
        # return [node.val if node else '#' for node in nodes]
        return nodes[0]



root = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(3)
node4 = TreeNode(5)
node5 = TreeNode(6)

root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
node4.right = node5

soln = Solution()
data = soln.serialize(root)
print data
# print soln.deserialize(data)
print soln.serialize(soln.deserialize(data))