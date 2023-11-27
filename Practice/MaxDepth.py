# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(root) -> int:
        
        if root is None:
            return 0
        
        left_depth = Solution.maxDepth(root.left)
        right_depth = Solution.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

# Example 1
# Create the binary tree [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(Solution.maxDepth(root1))  # Output: 3

# Example 2
# Create the binary tree [1,null,2]
root2 = TreeNode(1)
root2.right = TreeNode(2)
print(Solution.maxDepth(root2))  # Output: 2