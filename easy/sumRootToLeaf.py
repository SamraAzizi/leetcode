# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the current sum by shifting left and adding the current node's value
            current_sum = (current_sum << 1) | node.val
            
            # If it's a leaf node, return the current sum
            if not node.left and not node.right:
                return current_sum
            
            # Continue DFS on left and right children
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)