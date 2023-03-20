# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # streak wste new
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def uff(arr, start, end):
            if  start > end:
                return
        
            if start == end:
                return TreeNode(arr[start])

            mid = start + (end - start) // 2

            newnode = TreeNode(arr[mid])

            newnode.left = uff(arr, start ,mid - 1)
            newnode.right = uff(arr, mid + 1 ,end )

            return newnode

        

        return uff(nums,0, len(nums) -1)