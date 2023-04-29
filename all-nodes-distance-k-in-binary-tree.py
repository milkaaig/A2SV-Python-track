# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self, root, prevNodes):
        if not root: return

        if root.val == self.target:
            k = self.k
            self.calculator(root.right, k - 1, None)
            self.calculator(root.left, k - 1, None)

            if k == 0:
                self.calculator(root, k, None)

            avoid = root
            while prevNodes and k >= 0:
                k -= 1
                nextAvoid = prevNodes.pop()
                self.calculator(nextAvoid, k, avoid)
                avoid = nextAvoid
        else:
            prevNodes.append(root)
            self.traversal(root.left, prevNodes)
            self.traversal(root.right, prevNodes)
            if prevNodes:
                prevNodes.pop()

    def calculator(self, root, k, avoid):
        if not root:
            return
        
        if k == 0: 
            self.ans.append(root.val)
        elif k > 0:
            k -= 1
            if root.left is not avoid:
                self.calculator(root.left, k, None)
            if root.right is not avoid:
                self.calculator(root.right, k, None)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.k = k
        self.target = target.val
        self.ans = []
        self.traversal(root, [])
        return self.ans