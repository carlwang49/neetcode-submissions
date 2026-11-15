# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # Check current node
        if root.val == subRoot.val and self.check_identical(root, subRoot):
            return True          
        
        # Find left child and right child
        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)

        return left_check or right_check

    def check_identical(self, root1, root2):
        # recursive check
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if not root2 and root1:
            return False
        if root1.val != root2.val:
            return False
        else:
            left_check = self.check_identical(root1.left, root2.left)
            right_check = self.check_identical(root1.right, root2.right)
        return left_check and right_check
            