from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # write code here7
        tmp = []
        if root is None:
            return tmp
        queue = [root]
        while queue:
            nodes = []
            next_nodes = []
            for node in queue:
                nodes.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            tmp.append(nodes)
            queue = next_nodes
        return tmp

root = TreeNode([1,2])

s = Solution()
s.levelOrder(root)