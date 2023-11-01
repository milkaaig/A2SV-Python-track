# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        
        def trav(node):
            if node:
                if node.val in dic:
                    dic[node.val] += 1
                else:
                    dic[node.val] = 1
                trav(node.right)
                trav(node.left)
        
        trav(root)
        output = []
        freq = max(dic.values())
        
        for key, val in dic.items():
            if val == freq:
                output.append(key)
        return output
        