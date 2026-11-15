# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def find_num(root, target, path):
            if root.val == target:
                path.append(target)
                return path
            path.append(root.val)
            if target < root.val:      
                return find_num(root.left, target, path)
            else:
                return find_num(root.right, target, path)
        
        p_path = find_num(root, p.val, [])
        q_path = find_num(root, q.val, [])
        flag = False
        for i in range(len(p_path)-1, -1, -1):
            for j in range(len(q_path)-1, -1, -1):
                if p_path[i] == q_path[j]:
                    flag = True
                    ans = p_path[j]
                    break
            if flag:
                break

        def find_node(root, target):
            if root.val == target:
                return root
            if target < root.val:      
                return find_node(root.left, target)
            else:
                return find_node(root.right, target)        

        return find_node(root, ans)






