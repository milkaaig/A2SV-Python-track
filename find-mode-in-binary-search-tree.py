# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        mapp = defaultdict(int)

        def inorder(node):
            if node:
                inorder(node.left)
                mapp[node.val] += 1
                inorder(node.right)
        inorder(root)

        m = 0
        val = []

        for k, v in mapp.items():
            if v > m:
                m = v
                val = k

        
        output = []
      

        for k ,v in mapp.items():
            if v == m:
                output.append(k)

        return output