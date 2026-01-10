# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, roots):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total = 0
        self.res = 0
        MOD = 10**9 + 7
        
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_sum = left_sum + right_sum + node.val
            self.total += node.val
            return curr_sum
        
        def find_max_product(node):
            if not node:
                return 0
            left_sum = find_max_product(node.left)
            right_sum = find_max_product(node.right)
            curr_sum = left_sum + right_sum + node.val
            
            # Calculate the product of the current subtree sum and the rest of the tree
            product = curr_sum * (self.total - curr_sum)
            self.res = max(self.res, product)
            
            return curr_sum
        
        dfs(roots)
        find_max_product(roots)
        
        return self.res % MOD