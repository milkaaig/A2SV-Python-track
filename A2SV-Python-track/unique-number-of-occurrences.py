class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        
        for num in arr:
            freq[num] += 1
        
        checker = set()
        
        for key, val in freq.items():
            if val in checker:
                return False
            checker.add(val)
        
        return True
            