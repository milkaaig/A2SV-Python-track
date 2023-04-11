"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
            
        def Depth(node):

            if not node.children:
                return 1

            count = 0
            for child in node.children:
                count = max(Depth( child), count ) 
                

            return count + 1
        
        return Depth(root)