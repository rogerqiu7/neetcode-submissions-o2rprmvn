# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            max_left = dfs(node.left)
            max_right = dfs(node.right)

            current = max_left + max_right

            res = max(current,res)

            return 1 + max(max_left, max_right)

        dfs(root)
        return res