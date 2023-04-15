# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def pathSum(node, path, output):
            if node:
                if not node.right and not node.left:
                    print(sum(path))
                    path = path + [node.val]
                    if sum(path) == targetSum:
                        output.append(path[:])
                        return

                
                pathSum(node.left, path + [node.val], output)
            
                pathSum(node.right, path + [node.val], output)
        
        pathSum(root, [], output)

        return output