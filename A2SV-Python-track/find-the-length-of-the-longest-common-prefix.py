class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        maxLength = 0
        possPrefixes = set()
        
        
        for prefix in arr1:
            while prefix not in possPrefixes and prefix > 0:
                possPrefixes.add(prefix)
                
                prefix //= 10
                
                
        for prefix in arr2:
            while prefix not in possPrefixes and prefix > 0:
                prefix //= 10
            
            if prefix > 0:
                maxLength = max(maxLength, len(str(prefix))) 
                
        return maxLength
                
                
                
