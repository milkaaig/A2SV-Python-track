# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        output = []
        to_delete = set(to_delete)
        
        def delete(node):
            if node:
                
                node.left = delete(node.left)
                node.right = delete(node.right)
                
                if not node.left and not node.right and node.val in to_delete:
                    return None
                elif node.val in to_delete:
                    if node.left:
                        output.append(node.left)
                    if node.right:
                        output.append(node.right)
                    return None
                
                return node
            
        is_root = delete(root)
        
        
        if is_root:
            output.append(is_root)
        
        return output
        
                
               