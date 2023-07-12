
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):

        if root is None:
            result=0
            print(result)
            return result
        else:
            queue = [(root, 1)]

            while queue:
                node, depth = queue.pop(0)

                if node.left is None and node.right is None:
                    return depth

                if node.left is not None:
                    queue.append((node.left, depth + 1))

                if node.right is not None:
                    queue.append((node.right, depth + 1))
            return 0

object = Solution()
root = TreeNode(1)
min_depth = object.minDepth(root)
