# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0 # Diameter 

        def max_depth(node):
            if not node:
                return 0

            left = max_depth(node.left)
            right = max_depth(node.right)

            # 更新直徑（這才是重點）=> 計算每個點當做 root 的直徑
            self.ans = max(self.ans, left + right)

            # 回傳每個節點當作 root 的最大高度
            return max(left, right) + 1

        x = max_depth(root)
        return self.ans