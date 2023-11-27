class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def removeLeafNodes(root, target):
        def isLeaf(node):
            return not node.left and not node.right
        
        if not root:
            return None
        
        root.left = TreeNode.removeLeafNodes(root.left, target)
        root.right = TreeNode.removeLeafNodes(root.right, target)

        if TreeNode.isLeaf(root) and root.val == target:
            return None
        else:
            return root 