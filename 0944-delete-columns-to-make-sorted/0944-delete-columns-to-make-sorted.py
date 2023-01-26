from collections import defaultdict 
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
       
        count = 0
        size = len(strs)
        for i in zip(*strs):
            if list(i) != sorted(i):
                count += 1
        return count
            